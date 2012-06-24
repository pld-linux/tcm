Summary:	A suite of graphical editors for diagrams and tables
Summary(pl):	Zestaw graficznych edytor�w do diagram�w i tabel
Name:		tcm
Version:	2.20
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.cs.utwente.nl/pub/tcm/%{name}-%{version}.src.tar.gz
# Source0-md5:	ed9b7135995ff57c3ff0fea57b8b55c6
Patch0:		%{name}-shared.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-install.patch
Patch3:		%{name}-text2ps.patch
Patch4:		%{name}-fonts.patch
URL:		http://wwwhome.cs.utwente.nl/~tcm/
BuildRequires:	X11-devel
# don't use lesstif here, as it's known to cause problems
BuildRequires:	openmotif-devel
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

%description -l pl
TCM (Toolkit for Conceptual Modeling) to zbi�r program�w narz�dziowych
do prezentacji modeli koncepcyjnych system�w programowych w postaci
diagram�w, tabel, drzew itp. Model koncepcyjny systemu to struktura
maj�ca reprezentowa� wymagania lub architektur� systemu. TCM ma s�u�y�
do okre�lania i utrzymywania wymaga� danych system�w, w kt�rych
u�ywane jest wiele technik i heurystyk do analizy problemu,
ulepszania funkcji, okre�lania zachowania i okre�lania architektury.
TCM przyjmuje posta� zestawu graficznych edytor�w, kt�rych mo�na
u�ywa� do tych zada� projektowych. Edytory te mo�na podzieli� na:

- edytory og�lne do og�lnych diagram�w, og�lnych tabel i og�lnych
  drzew,
- edytory do analizy strukturalnej (SA - Structured Analysis) dla
  diagram�w entity-relationship, diagram�w przep�ywu danych i zdarze�,
  diagram�w przej�� stan�w, drzew ulepszania funkcji, tabel
  transaction use oraz function-entity
- edytory UML (Unified Modeling Language) dla diagram�w struktur
  statycznych, diagram�w przypadk�w u�ycia, diagram�w aktywno�ci,
  wykres�w stan�w, diagram�w sekwencji komunikat�w, diagram�w
  wsp�pracy, diagram�w sk�adnik�w i diagram�w wdra�ania.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__make} config \
	OPTFLAGS="%{rpmcflags}" \
	TCM_INSTALL_DIR=%{_prefix}

%{__make} depend \
	OPTLAGS="%{rpmcflags}" \
	TCM_INSTALL_DIR=%{_prefix}

%{__make} execs \
	OPTFLAGS="%{rpmcflags}" \
	TCM_INSTALL_DIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
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
