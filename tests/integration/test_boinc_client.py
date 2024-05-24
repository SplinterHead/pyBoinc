from pytest import mark


# Messages
@mark.integration
def test_messages(boinc_session_client):
    result = boinc_session_client.get_messages()
    assert result
    assert "messages" in result


@mark.integration
def test_message_with_start(boinc_session_client):
    all_msg = boinc_session_client.get_messages()
    result = boinc_session_client.get_messages(start=1)
    assert result
    assert "messages" in result
    assert len(result["messages"]) == len(all_msg["messages"]) - 1


@mark.integration
def test_message_count(boinc_session_client):
    result = boinc_session_client.get_message_count()
    assert result
    assert "message_count" in result


@mark.integration
def test_public_notices(boinc_session_client):
    result = boinc_session_client.get_public_notices()
    assert result
    assert "notices" in result


# Projects
@mark.integration
def test_all_projects_list(boinc_session_client):
    result = boinc_session_client.get_all_projects()
    assert result
    assert "projects" in result


# Results
@mark.integration
def test_results(boinc_session_client):
    result = boinc_session_client.get_results()
    assert result
    assert "results" in result


@mark.integration
def test_old_results(boinc_session_client):
    result = boinc_session_client.get_old_results()
    assert result
    assert "old_results" in result


# Stats
@mark.integration
def test_network_stats(boinc_session_client):
    result = boinc_session_client.get_network_stats()
    assert result
    assert "network_transfers" in result


@mark.integration
def test_project_stats(boinc_session_client):
    result = boinc_session_client.get_project_stats()
    assert result
    assert "project_stats" in result


# Status
@mark.integration
def test_client_state(boinc_session_client):
    result = boinc_session_client.get_client_state()
    assert result
    assert "client_state" in result


@mark.integration
def test_project_status(boinc_session_client):
    result = boinc_session_client.get_project_status()
    assert result
    assert "project_status" in result


@mark.integration
def test_cc_state(boinc_session_client):
    result = boinc_session_client.get_cc_status()
    assert result
    assert "cc_status" in result


@mark.integration
def test_disk_stats(boinc_session_client):
    result = boinc_session_client.get_disk_stats()
    assert result
    assert "disk_stats" in result


@mark.integration
def test_file_transfers(boinc_session_client):
    result = boinc_session_client.get_file_transfers()
    assert result
    assert "file_transfers" in result


@mark.integration
def test_host_info(boinc_session_client):
    result = boinc_session_client.get_host_info()
    assert result
    assert "host_info" in result


@mark.integration
def test_simple_gui_info(boinc_session_client):
    result = boinc_session_client.get_simple_gui_info()
    assert result
    assert "gui_info" in result


@mark.integration
def test_screensaver_tasks(boinc_session_client):
    result = boinc_session_client.get_screensaver_tasks()
    assert result
    assert "screensaver_tasks" in result


# Versions
@mark.integration
def test_container_version(boinc_session_client):
    result = boinc_session_client.get_client_version()
    assert result
    assert result is not {}


@mark.integration
def test_container_update(boinc_session_client):
    result = boinc_session_client.get_client_update()
    assert result
    assert "update" in result


@mark.integration
def test_global_preferences(boinc_session_client):
    result = boinc_session_client.get_global_prefs_file()
    assert result
    assert "error" in result  # No global_preferences file available


@mark.authenticated
def test_can_attach_and_detach_project(boinc_test_client, project_weak_key):
    assert (
        boinc_test_client.poll_attach_project()["project_attach_reply"]["error_num"]
        == 0
    )
    assert (
        boinc_test_client.get_project_status()["project_status"][0]["project_name"]
        == "World Community Grid"
    )
    boinc_test_client.detach_project("https://www.worldcommunitygrid.org/")
    assert len(boinc_test_client.get_client_state()["client_state"]["projects"]) == 0


@mark.authenticated
def test_can_attach_and_update_project(boinc_test_client, project_weak_key):
    pre_update_time = boinc_test_client.get_client_state()["client_state"][
        "time_stats"
    ]["now"]
    boinc_test_client.update_project("https://www.worldcommunitygrid.org/")
    post_update_time = boinc_test_client.get_client_state()["client_state"][
        "time_stats"
    ]["now"]
    assert pre_update_time < post_update_time


@mark.authenticated
def test_can_attach_and_reset_project(boinc_test_client, project_weak_key):
    pre_update_time = boinc_test_client.get_client_state()["client_state"][
        "time_stats"
    ]["now"]
    boinc_test_client.reset_project("https://www.worldcommunitygrid.org/")
    post_update_time = boinc_test_client.get_client_state()["client_state"][
        "time_stats"
    ]["now"]
    assert pre_update_time < post_update_time


@mark.authenticated
def test_can_attach_to_multiple_projects(boinc_test_client, project_weak_key):
    boinc_test_client.attach_project(
        "Space Community Grid",
        "https://www.spacecommunitygrid.org/",
        project_weak_key,
    )
    assert (
        boinc_test_client.poll_attach_project()["project_attach_reply"]["error_num"]
        == 0
    )
    assert (
        boinc_test_client.get_project_status()["project_status"][0]["project_name"]
        == "Space Community Grid"
    )
    assert (
        boinc_test_client.get_project_status()["project_status"][1]["project_name"]
        == "World Community Grid"
    )


@mark.authenticated
def test_can_suspend_and_resume_project(boinc_test_client, project_weak_key):
    boinc_test_client.suspend_project("https://www.worldcommunitygrid.org/")
    assert boinc_test_client.get_project_status()["project_status"][0][
        "suspended_via_gui"
    ]

    boinc_test_client.resume_project("https://www.worldcommunitygrid.org/")
    assert not boinc_test_client.get_project_status()["project_status"][0][
        "suspended_via_gui"
    ]


@mark.authenticated
def test_can_set_and_unset_nomorework_on_project(boinc_test_client, project_weak_key):
    boinc_test_client.project_no_more_work("https://www.worldcommunitygrid.org/")
    assert boinc_test_client.get_project_status()["project_status"][0][
        "dont_request_more_work"
    ]

    boinc_test_client.project_allow_more_work("https://www.worldcommunitygrid.org/")
    assert not boinc_test_client.get_project_status()["project_status"][0][
        "dont_request_more_work"
    ]


@mark.authenticated
def test_can_read_all_notices(boinc_test_client, project_weak_key):
    assert "notices" in boinc_test_client.get_all_notices()


@mark.authenticated
def test_can_write_and_read_global_preferences(boinc_test_client, project_weak_key):
    assert "error" in boinc_test_client.get_global_prefs_override()
    assert (
        boinc_test_client.get_global_prefs_working()["global_preferences"][
            "max_ncpus_pct"
        ]
        == 0.0
    )
    boinc_test_client.set_global_prefs_override({"max_ncpus_pct": 10})
    boinc_test_client.read_global_prefs_override()
    assert boinc_test_client.get_global_prefs_override()
    assert (
        boinc_test_client.get_global_prefs_working()["global_preferences"][
            "max_ncpus_pct"
        ]
        == 10.0
    )


@mark.authenticated
def test_can_sequentially_set_global_overrides(boinc_test_client, project_weak_key):
    boinc_test_client.set_global_prefs_override({"max_ncpus_pct": 10})
    boinc_test_client.read_global_prefs_override()
    boinc_test_client.update_global_prefs_override({"cpu_usage_limit": 10})
    boinc_test_client.read_global_prefs_override()
    assert (
        boinc_test_client.get_global_prefs_working()["global_preferences"][
            "max_ncpus_pct"
        ]
        == 10.0
    )
    assert (
        boinc_test_client.get_global_prefs_working()["global_preferences"][
            "cpu_usage_limit"
        ]
        == 10.0
    )


@mark.authenticated
def test_can_set_compute_modes(boinc_test_client, project_weak_key):
    assert boinc_test_client.set_cpu_run_mode("always", 60) == {"success": True}
    assert boinc_test_client.set_gpu_run_mode("auto", 0) == {"success": True}
    assert boinc_test_client.set_network_mode("never") == {"success": True}
