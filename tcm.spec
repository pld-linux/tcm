Summary:	A suite of graphical editors for diagrams and tables
Summary(pl.UTF-8):	Zestaw graficznych edytorów do diagramów i tabel
Name:		tcm
Version:	2.20
Release:	4
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.cs.utwente.nl/pub/tcm/%{name}-%{version}.src.tar.gz
# Source0-md5:	ed9b7135995ff57c3ff0fea57b8b55c6
Patch0:		%{name}-shared.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-install.patch
Patch3:		%{name}-text2ps.patch
Patch4:		%{name}-fonts.patch
Patch5:		%{name}-gcc4.patch
Patch6:		%{name}-missing-sentinel.patch
Patch7:		%{name}-export-png.patch
Patch8:		%{name}-gv-preview.patch
Patch9:		%{name}-quote-system-call.patch
Patch10:	%{name}-flex.patch
Patch100:	%{name}-TSQD.patch
URL:		http://wwwhome.cs.utwente.nl/~tcm/
BuildRequires:	flex
BuildRequires:	libstdc++-devel
# don't use lesstif here, as it's known to cause problems
BuildRequires:	openmotif-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libICE-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Toolkit for Conceptual Modeling is a collection of software tools
to present conceptual models of software systems in the form of
diagrams, tables, trees, and the like. A conceptual model of a system
is a structure used to represent the requirements or architecture of
the system. TCM is meant to be used for specifying and maintaining
requirements for desired systems, in which a number of techniques and
heuristics for problem analysis, function refinement, behavior
specification, and architecture specification are used. TCM takes
the form of a suite of graphical editors that can be used in these
design tasks. These editors can be categorized into:

* Generic editors, for generic diagrams, generic tables and
  generic trees.
* Structured Analysis (SA) editors, for entity-relationship diagrams,
  data and event flow diagrams, state transition diagrams, function
  refinement trees, transaction-use tables and function-entity
  type tables.
* Unified Modeling Language (UML) editors, for static structure
  diagrams, use-case diagrams, activity diagrams, state charts,
  message sequence diagrams, collaboration diagrams, component
  diagrams and deployment diagrams.

%description -l pl.UTF-8
TCM (Toolkit for Conceptual Modeling) to zbiór programów narzędziowych
do prezentacji modeli koncepcyjnych systemów programowych w postaci
diagramów, tabel, drzew itp. Model koncepcyjny systemu to struktura
mająca reprezentować wymagania lub architekturę systemu. TCM ma służyć
do określania i utrzymywania wymagań danych systemów, w których
używane jest wiele technik i heurystyk do analizy problemu,
ulepszania funkcji, określania zachowania i określania architektury.
TCM przyjmuje postać zestawu graficznych edytorów, których można
używać do tych zadań projektowych. Edytory te można podzielić na:

- edytory ogólne do ogólnych diagramów, ogólnych tabel i ogólnych
  drzew,
- edytory do analizy strukturalnej (SA - Structured Analysis) dla
  diagramów entity-relationship, diagramów przepływu danych i zdarzeń,
  diagramów przejść stanów, drzew ulepszania funkcji, tabel
  transaction use oraz function-entity
- edytory UML (Unified Modeling Language) dla diagramów struktur
  statycznych, diagramów przypadków użycia, diagramów aktywności,
  wykresów stanów, diagramów sekwencji komunikatów, diagramów
  współpracy, diagramów składników i diagramów wdrażania.

%prep
%setup -q
%patch100 -p1
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
%{__make} -j1 config \
	OPTFLAGS="%{rpmcflags}" \
	TCM_INSTALL_DIR=%{_prefix}

%{__make} -j1 depend \
	OPTLAGS="%{rpmcflags}" \
	TCM_INSTALL_DIR=%{_prefix}

%{__make} -j1 execs \
	OPTFLAGS="%{rpmcflags}" \
	TCM_INSTALL_DIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	TCM_INSTALL_DIR=%{_prefix}

# silence rpm
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/tcm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG FILEMAP README
%doc doc/usersguide* doc/wishlist
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/help
%{_datadir}/%{name}/help/[D-Z]*
%{_mandir}/man1/*
