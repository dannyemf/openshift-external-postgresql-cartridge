Summary:        Utility scripts for the OpenShift Origin broker and node
Name:           openshift-origin-util
Version: 1.0.3
Release:        1%{?dist}
Group:          Network/Daemons
License:        ASL 2.0
URL:            http://openshift.redhat.com
Source0:        http://mirror.openshift.com/pub/openshift-origin/source/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
This package contains a set of utility scripts for the broker and node. 

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
cp oo-* %{buildroot}%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0755,-,-) %{_bindir}/oo-ruby
%attr(0755,-,-) %{_bindir}/oo-exec-ruby
%attr(0755,-,-) %{_bindir}/oo-diagnostics


%changelog
* Wed Nov 21 2012 Dan McPherson <dmcphers@redhat.com> 1.0.3-1
- 

* Wed Nov 21 2012 Dan McPherson <dmcphers@redhat.com> 1.0.2-1
- new package built with tito

* Wed Nov 21 2012 Dan McPherson <dmcphers@redhat.com> 1.0.1-1
- new package built with tito

* Wed Nov 21 2012 Dan McPherson <dmcphers@redhat.com> 1.0.0-1
- Initial commit
