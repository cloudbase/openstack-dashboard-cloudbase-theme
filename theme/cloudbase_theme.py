# The presence of this file in /etc/openstack-dashboard/ and/or
# /usr/share/openstack-dashboard/openstack_dashboard/local/ will
# enable the Cloudbase theme for Horizon. To disable, remove the
# openstack-dashboard-cloudbase-theme package, or remove this file.
import os

CLOUDBASE_THEME = "/usr/share/openstack-dashboard-cloudbase-theme/static/themes/cloudbase"

if os.path.exists(CLOUDBASE_THEME):
    AVAILABLE_THEMES = [
        ('cloudbase', 'Cloudbase', CLOUDBASE_THEME),
    ]

