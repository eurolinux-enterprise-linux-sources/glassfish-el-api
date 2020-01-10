%global artifactId javax.el-api

Name:           glassfish-el-api
Version:        2.2.4
Release:        4%{?dist}
Summary:        Expression Language API 2.2.4

Group:          Development/Libraries
# Part of implementation files contain ASL 2.0 copyright
License:        CDDL and ASL 2.0
URL:            http://uel.java.net
# svn export https://svn.java.net/svn/uel~svn/tags/javax.el-api-2.2.4 javax.el-api-2.2.4
# tar cvJf javax.el-api-2.2.4.tar.xz javax.el-api-2.2.4/
Source0:        %{artifactId}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        generate_tarball.sh
BuildArch:      noarch

BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  jpackage-utils
BuildRequires:  jvnet-parent
BuildRequires:  maven-local
BuildRequires:  maven
BuildRequires:  maven-source-plugin

%description
This project provides an implementation of the Expression Language (EL). 
The main goals are:
 * Improves current implementation: bug fixes and performance improvements
 * Provides API for use by other tools, such as Netbeans

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{artifactId}-%{version}
cp -p %{SOURCE1} .

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 2.2.4-4
- Migrate away from mvn-rpmbuild (Resolves: #997498)

* Fri Aug 02 2013 Michal Srb <msrb@redhat.com> - 2.2.4-3
- Add generate_tarball.sh script to SRPM

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.4-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Jan 31 2013 David Xie <david.scriptfan@gmail.com> - 2.2.4-1
- Initial version of package
