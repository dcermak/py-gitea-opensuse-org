# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from py_gitea_opensuse_org.api.activitypub_api import ActivitypubApi
    from py_gitea_opensuse_org.api.admin_api import AdminApi
    from py_gitea_opensuse_org.api.issue_api import IssueApi
    from py_gitea_opensuse_org.api.miscellaneous_api import MiscellaneousApi
    from py_gitea_opensuse_org.api.notification_api import NotificationApi
    from py_gitea_opensuse_org.api.organization_api import OrganizationApi
    from py_gitea_opensuse_org.api.package_api import PackageApi
    from py_gitea_opensuse_org.api.repository_api import RepositoryApi
    from py_gitea_opensuse_org.api.settings_api import SettingsApi
    from py_gitea_opensuse_org.api.user_api import UserApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from py_gitea_opensuse_org.api.activitypub_api import ActivitypubApi
from py_gitea_opensuse_org.api.admin_api import AdminApi
from py_gitea_opensuse_org.api.issue_api import IssueApi
from py_gitea_opensuse_org.api.miscellaneous_api import MiscellaneousApi
from py_gitea_opensuse_org.api.notification_api import NotificationApi
from py_gitea_opensuse_org.api.organization_api import OrganizationApi
from py_gitea_opensuse_org.api.package_api import PackageApi
from py_gitea_opensuse_org.api.repository_api import RepositoryApi
from py_gitea_opensuse_org.api.settings_api import SettingsApi
from py_gitea_opensuse_org.api.user_api import UserApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
