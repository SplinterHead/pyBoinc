from boinc_client.clients.rpc_client import RpcClient

from .messages import get_all_notices, message_count, messages, public_notices
from .modes import set_cpu_run_mode, set_gpu_run_mode, set_network_mode
from .network import get_proxy_settings
from .preferences import (
    get_global_prefs_file,
    get_global_prefs_override,
    get_global_prefs_working,
    read_global_prefs_override,
    set_global_prefs_override,
    update_global_prefs_override,
)
from .projects import (
    all_projects,
    attach_project,
    detach_project,
    poll_attach_project,
    project_allow_more_work,
    project_no_more_work,
    reset_project,
    resume_project,
    suspend_project,
    update_project,
)
from .results import old_results, results
from .stats import daily_network_transfers, project_stats
from .status import (
    cc_status,
    client_state,
    disk_stats,
    file_transfers,
    host_info,
    project_status,
    screensaver_tasks,
    simple_gui_info,
)
from .versions import client_update, client_version


class Boinc:
    rpc_client: RpcClient

    def __init__(self, rpc_client: RpcClient):
        self.rpc_client = rpc_client

    ###########
    # Messages
    ###########
    def get_messages(self, start: int = 0) -> dict:
        return messages(client=self.rpc_client, start=start)

    def get_message_count(self) -> dict:
        return message_count(client=self.rpc_client)

    def get_public_notices(self, start: int = 0) -> dict:
        return public_notices(client=self.rpc_client, start=start)

    def get_all_notices(self, start: int = 0) -> dict:
        return get_all_notices(client=self.rpc_client, start=start)

    ###########
    # Projects
    ###########
    def get_all_projects(self) -> dict:
        return all_projects(client=self.rpc_client)

    def attach_project(self, name: str, url: str, key: str) -> dict:
        return attach_project(self.rpc_client, name, url, key)

    def poll_attach_project(self):
        return poll_attach_project(self.rpc_client)

    def update_project(self, url: str) -> dict:
        return update_project(self.rpc_client, url)

    def detach_project(self, url: str) -> dict:
        return detach_project(self.rpc_client, url)

    def suspend_project(self, url: str) -> dict:
        return suspend_project(self.rpc_client, url)

    def resume_project(self, url: str) -> dict:
        return resume_project(self.rpc_client, url)

    def reset_project(self, url: str) -> dict:
        return reset_project(self.rpc_client, url)

    ##########
    # Results
    ##########
    def get_results(self, active_only: bool = False) -> dict:
        return results(client=self.rpc_client, active_only=active_only)

    def get_old_results(self) -> dict:
        return old_results(client=self.rpc_client)

    ########
    # Stats
    ########
    def get_network_stats(self) -> dict:
        return daily_network_transfers(client=self.rpc_client)

    def get_project_stats(self) -> dict:
        return project_stats(client=self.rpc_client)

    #########
    # Status
    #########
    def get_client_state(self) -> dict:
        return client_state(client=self.rpc_client)

    def get_project_status(self) -> dict:
        return project_status(client=self.rpc_client)

    def get_cc_status(self) -> dict:
        return cc_status(client=self.rpc_client)

    def get_disk_stats(self) -> dict:
        return disk_stats(client=self.rpc_client)

    def get_file_transfers(self) -> dict:
        return file_transfers(client=self.rpc_client)

    def get_host_info(self) -> dict:
        return host_info(client=self.rpc_client)

    def get_simple_gui_info(self) -> dict:
        return simple_gui_info(client=self.rpc_client)

    def get_screensaver_tasks(self) -> dict:
        return screensaver_tasks(client=self.rpc_client)

    ########
    # Tasks
    ########
    def project_no_more_work(self, url: str) -> dict:
        return project_no_more_work(client=self.rpc_client, project_url=url)

    def project_allow_more_work(self, url: str) -> dict:
        return project_allow_more_work(client=self.rpc_client, project_url=url)

    ###########
    # Versions
    ###########
    def get_client_version(self) -> dict:
        return client_version(client=self.rpc_client)

    def get_client_update(self) -> dict:
        return client_update(client=self.rpc_client)

    ##############
    # Preferences
    ##############
    def get_global_prefs_file(self) -> dict:
        return get_global_prefs_file(self.rpc_client)

    def get_global_prefs_override(self) -> dict:
        return get_global_prefs_override(self.rpc_client)

    def set_global_prefs_override(self, pref_override: dict) -> None:
        return set_global_prefs_override(self.rpc_client, pref_override)

    def update_global_prefs_override(self, pref_override: dict) -> None:
        return update_global_prefs_override(self.rpc_client, pref_override)

    def get_global_prefs_working(self) -> dict:
        return get_global_prefs_working(self.rpc_client)

    def read_global_prefs_override(self) -> dict:
        return read_global_prefs_override(self.rpc_client)

    def set_cpu_run_mode(self, run_mode: str, duration: int = 0) -> dict:
        return set_cpu_run_mode(self.rpc_client, run_mode, duration)

    def set_gpu_run_mode(self, run_mode: str, duration: int = 0) -> dict:
        return set_gpu_run_mode(self.rpc_client, run_mode, duration)

    def set_network_mode(self, run_mode: str, duration: int = 0) -> dict:
        return set_network_mode(self.rpc_client, run_mode, duration)

    def get_proxy_settings(self) -> dict:
        return get_proxy_settings(self.rpc_client)
