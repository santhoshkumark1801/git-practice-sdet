"""
test_feature.py - Practice file for interactive rebase exercises.
Make multiple small commits to this file, then practice squashing/rewording.
"""

import pytest


class TestReportingFeature:

    def test_generate_summary_report(self):
        """Summary report should list all passed/failed tests."""
        report = {
            "total": 10,
            "passed": 8,
            "failed": 2,
            "pass_rate": 80.0
        }
        assert report["total"] == report["passed"] + report["failed"]
        assert report["pass_rate"] == (report["passed"] / report["total"]) * 100

    def test_export_to_csv(self):
        """Report should be exportable to CSV format."""
        headers = ["test_name", "status", "duration"]
        row = ["test_login", "PASSED", "0.23s"]
        assert len(row) == len(headers)

    def test_export_to_html(self):
        """Report should be exportable to HTML format."""
        html_content = "<html><body><h1>Test Report</h1></body></html>"
        assert "<html>" in html_content
        assert "</html>" in html_content

    def test_empty_report(self):
        """An empty test run should return a valid (empty) report."""
        report = {"total": 0, "passed": 0, "failed": 0}
        assert report["total"] == 0
