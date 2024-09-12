#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.08.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kaddressbook
Summary:	KAddressbook
Name:		ka6-%{kaname}
Version:	24.08.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d1cc649857576d2098ee4fc97c528436
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	gpgme-c++-devel >= 1.8.0
BuildRequires:	ka6-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-search-devel >= %{kdeappsver}
BuildRequires:	ka6-grantleetheme-devel >= %{kdeappsver}
BuildRequires:	ka6-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	ka6-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka6-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka6-libkleo-devel >= %{kdeappsver}
BuildRequires:	ka6-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcmutils-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-prison-devel >= %{kframever}
BuildRequires:	kuserfeedback-devel
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAddressBook stores all the personal details of your family, friends
and other contacts.

Features

• Imports and exports to nearly every address book standard • Reads
.vcf format files, and can import and export vCards and csv format
files • Can use multiple LDAPservers • Configurable filters and
powerful search capabilities • Integrates with other Kontact
components, e.g. exporting Birthday reminders to KOrganizer • Capable
of groupware integration • Powered by Akonadi

%description -l pl.UTF-8
KAddressBook potrafi zachować szczegóły osobiste Twojej rodziny,
przyjaciół i inne kontakty.

Właściwości

• Importuje i eksportuje do niemalże każdego standardu książki
adresowej • Czyta pliki formatu .vcf, może importować i eksportować
pliki vCards i csv. • Może używać wielu serwerów LDAP • Konfigurowalne
filtry i duże możliwości wyszukiwania • Integruje się z innymi
komponentami Kontact, np. eksportując przypomnienia o urodzinach do
KOrganizera • Możliwość integracji z groupware • "Napędzane" przez
Akonadi

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ka5-%{kaname}-devel < %{version}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaddressbook
%attr(755,root,root) %{_libdir}/libKPim6AddressbookImportExport.so.*.*
%{_libdir}/libKPim6AddressbookImportExport.so.6
%attr(755,root,root) %{_libdir}/libkaddressbookprivate.so.*.*
%{_libdir}/libkaddressbookprivate.so.6
%attr(755,root,root) %{_libdir}/qt6/plugins/kaddressbookpart.so
%dir %{_libdir}/qt6/plugins/pim6/kcms/kaddressbook
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/kaddressbook/kaddressbook_config_plugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kontact/kontact_kaddressbookplugin.so
%{_desktopdir}/kaddressbook-importer.desktop
%{_desktopdir}/kaddressbook-view.desktop
%{_desktopdir}/org.kde.kaddressbook.desktop
%{_iconsdir}/hicolor/128x128/apps/kaddressbook.png
%{_iconsdir}/hicolor/16x16/apps/kaddressbook.png
%{_iconsdir}/hicolor/22x22/apps/kaddressbook.png
%{_iconsdir}/hicolor/32x32/apps/kaddressbook.png
%{_iconsdir}/hicolor/48x48/apps/kaddressbook.png
%{_iconsdir}/hicolor/64x64/apps/kaddressbook.png
%{_iconsdir}/hicolor/scalable/apps/kaddressbook.svg
%{_datadir}/kaddressbook
%{_datadir}/metainfo/org.kde.kaddressbook.appdata.xml
%{_datadir}/qlogging-categories6/kaddressbook.categories
%{_datadir}/qlogging-categories6/kaddressbook.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KPim6/KAddressBookImportExport
%{_libdir}/cmake/KPim6AddressbookImportExport
%{_libdir}/libKPim6AddressbookImportExport.so
