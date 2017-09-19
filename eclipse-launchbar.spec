%{?scl:%scl_package eclipse-launchbar}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 1

%global git_tag 	b57aa9d3362bd46460d9c4d3ac64ac4e9ac893d9

Epoch:          1
Name:           %{?scl_prefix}eclipse-launchbar
Version:        2.1.0
Release:        1.%{baserelease}%{?dist}
Summary:        Eclipse Launchbar plug-in
License:        EPL
URL:            https://wiki.eclipse.org/CDT/LaunchBar

Source0:        http://git.eclipse.org/c/cdt/org.eclipse.launchbar.git/snapshot/org.eclipse.launchbar-%{git_tag}.tar.xz

# Following patch to specify javax-annotation is no longer needed.
# Patch0: eclipse-launchbar-annotation.patch

BuildArch:      noarch

BuildRequires: %{?scl_prefix}tycho
BuildRequires: %{?scl_prefix}tycho-extras
BuildRequires: %{?scl_prefix}eclipse-pde
BuildRequires: %{?scl_prefix}eclipse-license
BuildRequires: %{?scl_prefix}eclipse-remote

%description
An alternative to the default launcher toolbar in Eclipse.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -q -n org.eclipse.launchbar-%{git_tag}
# %patch0 -p1
find -name *.jar -exec rm -rf {} \;
find -name *.class -exec rm -rf {} \;

%pom_disable_module repo
%pom_disable_module tests/org.eclipse.launchbar.core.tests
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_build -j
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles

%changelog
* Mon Jan 23 2017 Mat Booth <mat.booth@redhat.com> - 1:2.1.0-1.1
- Auto SCL-ise package for rh-eclipse46 collection

* Mon Jan 16 2017 Jeff Johnston <jjohnstn@redhat.com> - 1:2.1.0-1
- Update to Neon.2 release
- Remove javax.annotation patch

* Tue Oct 11 2016 Mat Booth <mat.booth@redhat.com> - 1:2.0.1-1.1
- Auto SCL-ise package for rh-eclipse46 collection

* Tue Oct 04 2016 Mat Booth <mat.booth@redhat.com> - 1:2.0.1-1
- Update to Neon.1 release

* Fri Jul 29 2016 Mat Booth <mat.booth@redhat.com> - 1:2.0.0-0.1.git1f95c6c.1
- Auto SCL-ise package for rh-eclipse46 collection

* Mon Apr 25 2016 Sopot Cela <scela@redhat.com> - 1:2.0.0-0.1.git1f95c6c
- Upstream version correction

* Mon Apr 25 2016 Sopot Cela <scela@redhat.com> - 1:1.0.1-2.git1f95c6c
- Upgrade for Neon

* Thu Mar 10 2016 Mat Booth <mat.booth@redhat.com> - 1:1.0.1-1.gitedd5f69
- Take a post-release snapshot of 1.0.1 due to API breakage in newer versions

* Thu Mar 03 2016 Sopot Cela <scela@redhat.com> - 1.0.2-0.1.git93cdb07
- Updated to 1.0.2 for Mars.2 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.2.git3c10977
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Sopot Cela <scela@redhat.com> - 1.0.1-0.1.git3c10977
- Updated to 1.0.1 for Mars.1 release

* Wed Jul 15 2015 Sopot Cela <scela@redhat.com> - 1.0.0-0.3.gite1ac200
- Added javax.annotation patch

* Tue Jun 16 2015 Alexander Kurtakov <akurtako@redhat.com> 1.0.0-0.2.git01bfa62
- New snapshot

* Wed Jun 3 2015 Sopot Cela <scela@redhat.com> - 1.0.0-0.1.gite1ac200
- Initial packaging
