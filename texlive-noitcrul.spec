Name:		texlive-noitcrul
Version:	0.2
Release:	1
Summary:	Improved underlines in mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/noitcrul
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noitcrul.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noitcrul.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noitcrul.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a (maths mode) \underline variant which
doesn't impose italics correction at the end.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
