Summary:	Graph - Editor and a Programming Environement
Name:		rocs
Version:	4.13.3
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
Url:		http://edu.kde.org/rocs
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	boost-devel
BuildRequires:	grantlee-devel

%description
Rocs aims to be a Graph Theory IDE for helping professors to show the results
of a graph algorithm and also helping students to do the algorithms.
Rocs has a scripting module, done in Qt Script, that interacts with the drawn
graph and every change in the graph with the script is reflected on the drawn
one.

%files
%doc AUTHORS COPYING COPYING.LIB.LGPL-2 COPYING.LIB.LGPL-2.1 COPYING.DOC README
%doc %{_kde_docdir}/HTML/en/rocs
%{_kde_bindir}/rocs
%{_kde_appsdir}/rocs
%{_kde_appsdir}/rocs_rootedtree
%{_kde_applicationsdir}/rocs.desktop
%{_kde_configdir}/rocs.knsrc
%{_kde_datadir}/config.kcfg/rocs.kcfg
%{_kde_iconsdir}/hicolor/*/apps/rocs.*
%{_kde_libdir}/kde4/rocs_GraphStructure.so
%{_kde_libdir}/kde4/rocs_ListStructure.so
%{_kde_libdir}/kde4/rocs_RootedTreeStructure.so
%{_kde_libdir}/kde4/rocs_assignvaluesplugin.so
%{_kde_libdir}/kde4/rocs_generategraphplugin.so
%{_kde_libdir}/kde4/rocs_transformedgesplugin.so
%{_kde_libdir}/kde4/rocs_dotfileformat.so
%{_kde_libdir}/kde4/rocs_gmlfileformat.so
%{_kde_libdir}/kde4/rocs_kmlfileformat.so
%{_kde_libdir}/kde4/rocs_tgffileformat.so
%{_kde_libdir}/kde4/rocs_tikzfileformat.so
%{_kde_services}/rocs_GraphStructure.desktop
%{_kde_services}/rocs_ListStructure.desktop
%{_kde_services}/rocs_RootedTreeStructure.desktop
%{_kde_services}/rocs_assignvaluesplugin.desktop
%{_kde_services}/rocs_generategraphplugin.desktop
%{_kde_services}/rocs_transformedgesplugin.desktop
%{_kde_services}/rocs_dotfileformatplugin.desktop
%{_kde_services}/rocs_gmlfileformatplugin.desktop
%{_kde_services}/rocs_kmlfileformatplugin.desktop
%{_kde_services}/rocs_tgffileformatplugin.desktop
%{_kde_services}/rocs_tikzfileformatplugin.desktop
%{_kde_servicetypes}/RocsDataStructurePlugin.desktop
%{_kde_servicetypes}/RocsGraphFilePlugin.desktop
%{_kde_servicetypes}/RocsToolsPlugin.desktop

#---------------------------------------------

%define rocsvisualeditor_major 4
%define librocsvisualeditor %mklibname rocsvisualeditor %{rocsvisualeditor_major}

%package -n %{librocsvisualeditor}
Summary:	Runtime library for Rocs
Group:		System/Libraries

%description -n %{librocsvisualeditor}
Runtime library for Rocs.

%files -n %{librocsvisualeditor}
%{_kde_libdir}/librocsvisualeditor.so.%{rocsvisualeditor_major}*

#---------------------------------------------

%define rocscore_major 4
%define librocscore %mklibname rocscore %{rocscore_major}

%package -n %{librocscore}
Summary:	Runtime library for Rocs
Group:		System/Libraries
Obsoletes:	%{_lib}rocslib4 < 4.10.0

%description -n %{librocscore}
Runtime library for Rocs.

%files -n %{librocscore}
%{_kde_libdir}/librocscore.so.%{rocscore_major}*


#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{librocsvisualeditor} = %{EVRD}
Requires:	%{librocscore} = %{EVRD}
Requires:	boost-devel
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_includedir}/rocs
%{_kde_libdir}/librocsvisualeditor.so
%{_kde_libdir}/librocscore.so

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.0-1
- New version 4.11.0
- Add grantlee-devel to BuildRequires
- Update files list

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.3-1
- New version 4.10.3
- Update files (add icons)

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0
- librocslib is replaced with librocscore and librocsvisualeditor
- Update files

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.97-1
- New version 4.8.97

* Tue Jul 10 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95
- Update files

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.8.0-1
+ Revision: 762504
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758089
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744568
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.90-1
+ Revision: 739323
- New upstream tarball $NEW_VERSION

* Thu Nov 24 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 733071
- New upstream tarball 4.7.80

* Wed Nov 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.41-1
+ Revision: 729219
- Import package

