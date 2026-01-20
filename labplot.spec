%global debug_package %{nil}

Summary:        LabPlot is a FREE, open source and cross-platform Data Visualization and Analysis software accessible to everyone
Name:		labplot
Version:	2.12.1
Release:	1
License:	GPLv2+
Group:		Sciences/Other
URL:		https://apps.kde.org/labplot/
Source0:	http://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Patch0:         2.12.1-fix-build-with-Qt-6.10.patch
Patch1:         2.12.1-add-missing-include.patch

BuildRequires:	bison
BuildRequires:	pkgconfig(gsl)
BuildRequires:	gettext-devel
BuildRequires:	shared-mime-info
BuildRequires:	docbook-dtd42-xml
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Purpose)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(KUserFeedbackQt6)
BuildRequires:	cmake(QXlsxQt6)
BuildRequires:	cmake(Cantor)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6SerialPort)
BuildRequires:	pkgconfig(Qt6Sql)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(matio)
BuildRequires:	pkgconfig(netcdf)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(liblz4)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	hdf5-devel
BuildRequires:	pkgconfig(poppler-qt6)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(libmarkdown)
BuildRequires:	pkgconfig(liborcus-0.21)
BuildRequires:	readstat-devel
BuildRequires:  pkgconfig(libcerf)
BuildRequires:  pkgconfig(libixion-0.20)
BuildRequires:  pkgconfig(eigen3)

BuildSystem:    cmake
BuildOption:    -DENABLE_REPRODUCIBLE:BOOL=ON

%description
LabPlot provides an easy way to create, manage and edit plots.
It allows you to produce plots based on data from a spreadsheet or on
data imported from external files.
Plots can be exported to several pixmap and vector graphic formats.


%find_lang %{name} --with-html

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license LICENSES/*
%{_bindir}/%{name}
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_iconsdir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_libdir}/lib%{name}.so*
%{_libdir}/cmake/%{name}/LabPlot*
%{_mandir}/man1/%{name}*.*
%{_includedir}/%{name}/*
