Name:           openstack-dashboard-cloudbase-theme
Version:        12.0.0
Release:        0
Summary:        Cloudbase Theme for the OpenStack Dashboard (Horizon)

License:        Apache 2.0
URL:            https://github.com/cloudbase/openstack-dashboard-cloudbase-theme/releases
Source0:        https://github.com/cloudbase/openstack-dashboard-cloudbase-theme/archive/%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-buildroot

Provides:       openstack-dashboard-cloudbase-theme = 12.0.0
Requires:       openstack-dashboard >= 12.0.0

%description
Provides a Cloudbase Solutions openstack-dashboard (Horizon) theme and overrides the default one.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase
mkdir -p $RPM_BUILD_ROOT/usr/share/openstack-dashboard/openstack_dashboard/local
cp -R $RPM_BUILD_DIR/%{name}-%{version}/theme/cloudbase/* $RPM_BUILD_ROOT/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755, root, root, -)
%dir %attr(0755, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase"
%dir %attr(0755, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/_styles.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/_variables.scss"
%dir %attr(0755, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/assets"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/assets/cloudbase-splash.svg"
%dir %attr(0755, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/bootstrap"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/bootstrap/_styles.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/bootstrap/_variable_customizations.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/bootstrap/_variables.scss"
%dir %attr(0755, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/_animations.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/_icons.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/_styles.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/_variables.scss"
%dir %attr(0755, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_checkboxes.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_context_selection.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_datepicker.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_dropdowns.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_hamburger.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_help_panel.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_loader_circular_example.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_loader_line_example.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_loader_spinner.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_magic_search.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_messages.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_navbar.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_progress_bars.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_radiobuttons.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_selects.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_sidebar.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_spinners.scss"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/horizon/components/_trees.scss"
%dir %attr(0755, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/js"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/static/js/material.hamburger.js"
%dir %attr(0755, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/templates"
%dir %attr(0755, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/templates/auth"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/templates/auth/_splash.html"
%dir %attr(0755, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/templates/cloudbase"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/templates/cloudbase/cloudbase-white-text.svg"
%dir %attr(0755, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/templates/header"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/templates/header/_brand.html"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/templates/header/_header.html"
%dir %attr(0755, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/templates/horizon"
%attr(0644, root, root) "/usr/share/openstack-dashboard/openstack_dashboard/themes/cloudbase/templates/horizon/_sidebar.html"
%exclude /usr/share/openstack-dashboard/openstack_dashboard/local/cloudbase_theme.pyc
%exclude /usr/share/openstack-dashboard/openstack_dashboard/local/cloudbase_theme.pyo

%post -p /bin/sh
#!/bin/sh

set -e

(
cat >>/etc/openstack-dashboard/local_settings <<'EOL'
# Cloudbase Theme Settings
AVAILABLE_THEMES = [
      (
          'cloudbase','Cloudbase','themes/cloudbase'
      ),
  ]
# End of Cloudbase Theme Settings
EOL
)
cd /usr/share/openstack-dashboard
echo "Collecting and compressing static assets..."
rm -f /usr/share/openstack-dashboard/openstack_dashboard/local/*.pyc || :
rm -f /usr/share/openstack-dashboard/static/custom/* || :
python manage.py collectstatic --noinput 2>&1 > /dev/null
python manage.py compress --force 2>&1 > /dev/null

echo "Restarting apache..."
service httpd restart

%postun -p /bin/sh
#!/bin/sh

set -e

(
  sed -i '/# Cloudbase/,/^$/d' /etc/openstack-dashboard/local_settings
  cd /usr/share/openstack-dashboard
  echo "Collecting and compressing static assets..."
  rm -f /usr/share/openstack-dashboard/openstack_dashboard/local/cloudbase_theme.pyc
  rm -f /usr/share/openstack-dashboard/static/custom/* || :
  python manage.py collectstatic --noinput 2>&1 > /dev/null
  python manage.py compress --force 2>&1 > /dev/null
)

echo "Restarting apache..."
service httpd restart

%changelog
* Thu Oct 5 2017 Dorin Paslaru
- 12.0.0 Pike release
* Wed Dec 21 2016 Dorin Paslaru
- 10.0.0 Newton release
* Fri Sep 16 2016 Dorin Paslaru
- 9.0.1 Mitaka second release; Minor fix to a path name
* Fri Jul 29 2016 Dorin Paslaru
- 9.0.0 Mitaka release
* Thu Mar 3 2016 Dorin Paslaru
- 1.1 Liberty release
* Tue Aug 18 2015 Dorin Paslaru
- 1.0 First release
