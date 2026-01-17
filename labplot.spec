Summary:	Plasma5-application for interactive graphing and analysis of scientific data
Name:		labplot
Version:	2.12.1
Release:	1
License:	GPLv2+
Group:		Sciences/Other
URL:		https://apps.kde.org/labplot/
Source0:	http://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
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
#BuildRequires:	cmake(KF6KDELibs4Support)
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

#patchlist
# cantor
#labplot-2.11.1-cantor.patch

%description
LabPlot provides an easy way to create, manage and edit plots.
It allows you to produce plots based on data from a spreadsheet or on
data imported from external files.
Plots can be exported to several pixmap and vector graphic formats.

%prep
%autosetup -p1
#cmake  -Wno-dev \
#	-DENABLE_CANTOR:BOOL=ON \
#	-DENABLE_REPRODUCIBLE:BOOL=ON \
#	-DENABLE_VECTOR_BLF:BOOL=OFF \
#	-GNinja

%build
%ninja_build -C build

%install
%ninja_install -C build

# We dont want right now devel files
rm -rf %{buildroot}%{_includedir}/labplot/

%find_lang labplot2 --with-html

%files -f labplot2.lang
%doc AUTHORS ChangeLog
%{_kde5_bindir}/labplot2
%{_kde5_datadir}/metainfo/org.kde.labplot2.appdata.xml
%{_kde5_iconsdir}/*
%{_kde5_datadir}/labplot2/
%{_kde5_applicationsdir}/org.kde.labplot2.desktop
%{_kde5_datadir}/mime/packages/labplot2.xml
%{_libdir}/liblabplot.so
%{_mandir}/*/man1/labplot*.*
%{_mandir}/man1/labplot*.*
