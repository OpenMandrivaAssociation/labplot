Summary:	Plasma5-application for interactive graphing and analysis of scientific data
Name:		labplot
Version:	2.4.0
Release:	1
License:	GPLv2+
Group:		Sciences/Other
URL:		https://edu.kde.org/labplot/
Source0:	http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}-kf5.tar.xz
BuildRequires:	pkgconfig(gsl)
BuildRequires:	gettext-devel
BuildRequires:	shared-mime-info
BuildRequires:	docbook-dtd42-xml
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KDELibs4Support)

BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)

BuildRequires:	pkgconfig(cfitsio)

%description
LabPlot provides an easy way to create, manage and edit plots.
It allows you to produce plots based on data from a spreadsheet or on
data imported from external files.
Plots can be exported to several pixmap and vector graphic formats.

%prep
%setup -q -n %{name}-%{version}-kf5
%apply_patches

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang labplot2 --with-html

%files -f labplot2.lang
%doc AUTHORS ChangeLog README
%{_kde5_sysconfdir}/xdg/labplot2_themes.knsrc
%{_kde5_bindir}/labplot2
%{_kde5_datadir}/metainfo/org.kde.labplot2.appdata.xml
%{_kde5_iconsdir}/*
%{_kde5_datadir}/labplot2/
%{_kde5_applicationsdir}/org.kde.labplot2.desktop
%{_kde5_datadir}/kxmlgui5/labplot2/
%{_kde5_datadir}/mime/packages/labplot2.xml

