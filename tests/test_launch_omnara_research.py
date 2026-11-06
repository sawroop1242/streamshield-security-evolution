import json
import os
import unittest
from unittest.mock import patch

from scripts.launch_omnara_research import LaunchError, build_agent_config, launch, validate_api_url


class FakeResponse:
    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return json.dumps({"agent": {"id": "agt_" + "a" * 26}}).encode()


class LaunchOmnaraResearchTests(unittest.TestCase):
    def test_config_is_read_only_research(self):
        config = build_agent_config("team-provider", "configured-model")
        self.assertEqual(config["model"]["provider_config"], "team-provider")
        self.assertEqual(set(config["tools"]), {"web_search", "web_fetch"})
        self.assertNotIn("machine_sources", config)
        self.assertIn("Do not modify repositories", config["instruction"])
        self.assertIn("external-camera recording are accepted limitations", config["instruction"])

    def test_api_url_requires_https_except_loopback(self):
        with self.assertRaises(LaunchError):
            validate_api_url("http://api.example.com/v1")
        self.assertEqual(validate_api_url("http://localhost:8080/api/v1"), "http://localhost:8080/api/v1")
        self.assertEqual(validate_api_url("https://api.omnara.com/v1/"), "https://api.omnara.com/v1")

    @patch.dict(os.environ, {
        "OMNARA_API_TOKEN": "test-token",
        "OMNARA_ORG_ID": "org_" + "a" * 26,
        "OMNARA_PROJECT_ID": "proj_" + "b" * 26,
        "OMNARA_MODEL_PROVIDER_CONFIG": "team-provider",
        "OMNARA_MODEL_NAME": "configured-model",
        "GITHUB_RUN_ID": "123456",
    }, clear=True)
    @patch("scripts.launch_omnara_research.urllib.request.urlopen", return_value=FakeResponse())
    def test_launch_posts_to_documented_endpoint(self, mock_urlopen):
        result = launch()
        self.assertTrue(result["agent_id"].startswith("agt_"))
        request = mock_urlopen.call_args.args[0]
        self.assertTrue(request.full_url.endswith(
            "/orgs/" + "org_" + "a" * 26 + "/projects/" + "proj_" + "b" * 26 + "/agents"
        ))
        self.assertEqual(request.get_header("Idempotency-key"), "streamshield-research-123456")
        body = json.loads(request.data)
        self.assertEqual(body["config_source"]["source_format"], "json")
        self.assertEqual(body["config_source"]["source"]["model"]["name"], "configured-model")

    @patch.dict(os.environ, {}, clear=True)
    def test_missing_credentials_fail_closed(self):
        with self.assertRaises(LaunchError):
            launch()


if __name__ == "__main__":
    unittest.main()
