# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/noitcrul
# catalog-date 2007-03-10 12:31:42 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-noitcrul
Version:	0.2
Release:	5
Summary:	Improved underlines in mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/noitcrul
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noitcrul.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noitcrul.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noitcrul.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 754351
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719124
- texlive-noitcrul
- texlive-noitcrul
- texlive-noitcrul
- texlive-noitcrul

