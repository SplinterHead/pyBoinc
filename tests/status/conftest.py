from pytest import fixture


@fixture
def basic_cc_status_xml() -> str:
    return """<cc_status>
        <network_status>2</network_status>
        <ams_password_error>0</ams_password_error>
        <task_suspend_reason>0</task_suspend_reason>
        <task_mode>2</task_mode>
        <task_mode_perm>2</task_mode_perm>
        <task_mode_delay>0.000000</task_mode_delay>
        <gpu_suspend_reason>0</gpu_suspend_reason>
        <gpu_mode>2</gpu_mode>
        <gpu_mode_perm>2</gpu_mode_perm>
        <gpu_mode_delay>0.000000</gpu_mode_delay>
        <network_suspend_reason>0</network_suspend_reason>
        <network_mode>2</network_mode>
        <network_mode_perm>2</network_mode_perm>
        <network_mode_delay>0.000000</network_mode_delay>
        <disallow_attach>0</disallow_attach>
        <simple_gui_only>0</simple_gui_only>
        <max_event_log_lines>2000</max_event_log_lines>
    </cc_status>"""


@fixture
def basic_cc_status_dict() -> dict:
    return {
        "cc_status": {
            "network_status": "2",
            "ams_password_error": "0",
            "task_suspend_reason": "0",
            "task_mode": "2",
            "task_mode_perm": "2",
            "task_mode_delay": "0.000000",
            "gpu_suspend_reason": "0",
            "gpu_mode": "2",
            "gpu_mode_perm": "2",
            "gpu_mode_delay": "0.000000",
            "network_suspend_reason": "0",
            "network_mode": "2",
            "network_mode_perm": "2",
            "network_mode_delay": "0.000000",
            "disallow_attach": "0",
            "simple_gui_only": "0",
            "max_event_log_lines": "2000",
        }
    }
