Summary:	Graph - Editor and a Programming Environement
Name:		rocs
Version:	15.04.3
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/rocs
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	grantlee-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(Grantlee5)

%description
Rocs aims to be a Graph Theory IDE for helping professors to show the results
of a graph algorithm and also helping students to do the algorithms.
Rocs has a scripting module, done in Qt Script, that interacts with the drawn
graph and every change in the graph with the script is reflected on the drawn
one.

%files
%doc AUTHORS COPYING COPYING.LIB.LGPL-2 COPYING.LIB.LGPL-2.1 COPYING.DOC README                                                                                    
%doc %{_docdir}/HTML/en/rocs                                                                           
%{_datadir}/applications/kde4/rocs.desktop                                                             
%{_datadir}/apps/rocs                                                                                  
%{_datadir}/apps/rocs_rootedtree                                                                       
%{_bindir}/rocs                                                                                        
%{_datadir}/config/rocs.knsrc                                                                          
%{_datadir}/appdata/rocs.appdata.xml                                                                   
%{_datadir}/config.kcfg/rocs.kcfg                                                                      
%{_iconsdir}/hicolor/*/apps/rocs.*                                                                     
%{_libdir}/kde4/rocs_GraphStructure.so                                                                 
%{_libdir}/kde4/rocs_ListStructure.so                                                                  
%{_libdir}/kde4/rocs_RootedTreeStructure.so                                                            
%{_libdir}/kde4/rocs_assignvaluesplugin.so                                                             
%{_libdir}/kde4/rocs_generategraphplugin.so                                                            
%{_libdir}/kde4/rocs_transformedgesplugin.so                                                           
%{_libdir}/kde4/rocs_dotfileformat.so                                                                  
%{_libdir}/kde4/rocs_gmlfileformat.so                                                                  
%{_libdir}/kde4/rocs_kmlfileformat.so                                                                  
%{_libdir}/kde4/rocs_tgffileformat.so                                                                  
%{_libdir}/kde4/rocs_tikzfileformat.so                                                                 
%{_datadir}/kde4/services/rocs_GraphStructure.desktop                                                  
%{_datadir}/kde4/services/rocs_ListStructure.desktop                                                   
%{_datadir}/kde4/services/rocs_RootedTreeStructure.desktop                                             
%{_datadir}/kde4/services/rocs_assignvaluesplugin.desktop                                              
%{_datadir}/kde4/services/rocs_generategraphplugin.desktop                                             
%{_datadir}/kde4/services/rocs_transformedgesplugin.desktop                                            
%{_datadir}/kde4/services/rocs_dotfileformatplugin.desktop                                             
%{_datadir}/kde4/services/rocs_gmlfileformatplugin.desktop                                             
%{_datadir}/kde4/services/rocs_kmlfileformatplugin.desktop                                             
%{_datadir}/kde4/services/rocs_tgffileformatplugin.desktop                                             
%{_datadir}/kde4/services/rocs_tikzfileformatplugin.desktop                                            
%{_datadir}/kde4/servicetypes/RocsDataStructurePlugin.desktop                                          
%{_datadir}/kde4/servicetypes/RocsGraphFilePlugin.desktop                                              
%{_datadir}/kde4/servicetypes/RocsToolsPlugin.desktop    

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
%{_libdir}/librocscore.so.%{rocscore_major}*

#---------------------------------------------

%package devel
Summary:	Development files for %{name}
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
%{_libdir}/librocsvisualeditor.so                                                                      
%{_libdir}/librocscore.so
#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
