%global tl_name noitcrul
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Improved underlines in mathematics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/noitcrul
License:	lppl1.3b
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noitcrul.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noitcrul.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noitcrul.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a (maths mode) \underline variant which doesn't
impose italics correction at the end.

