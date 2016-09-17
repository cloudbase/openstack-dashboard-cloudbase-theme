# Building a new RPM

Install necessary packages
```sh
sudo yum install -y rpmdevtools rpm-build
```
Generate the rpm environment
```sh
rpmdev-setuptree
```

Copy the spec file to the apropiate directory
```sh
wget -O rpmbuild/SPECS/openstack-dashboard-cloudbase-theme.spec https://raw.githubusercontent.com/cloudbase/openstack-dashboard-cloudbase-theme/rpm-build/rpmbuild/SPECS/openstack-dashboard-cloudbase-theme.spec
```
Now edit the file and make the apropiate changes (version, changelog etc.)

Download latest sources; Replace `$RPM_SOURCE_DIR` with your `rmpbuild/SOURCES` folder; Replace %{version} with the desired version from github
```sh
wget -O $RPM_SOURCE_DIR/%{version}.tar.gz https://github.com/cloudbase/openstack-dashboard-cloudbase-theme/archive/%{version}.tar.gz
```

Build the new RPM using:
```sh
rpmbuild -v -bb rpmbuild/SPECS/openstack-dashboard-cloudbase-theme.spec
```

if everything went fine, the finished RPM should be in `rpmbuild/RPMS` directory.
