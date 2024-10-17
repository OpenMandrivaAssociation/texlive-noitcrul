Name:		texlive-noitcrul
Version:	15878
Release:	2
Summary:	Improved underlines in mathematics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/noitcrul
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noitcrul.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noitcrul.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noitcrul.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a (maths mode) \underline variant which
doesn't impose italics correction at the end.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/noitcrul/noitcrul.sty
%doc %{_texmfdistdir}/doc/latex/noitcrul/README
%doc %{_texmfdistdir}/doc/latex/noitcrul/noitcrul.pdf
#- source
%doc %{_texmfdistdir}/source/latex/noitcrul/noitcrul.dtx
%doc %{_texmfdistdir}/source/latex/noitcrul/noitcrul.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
