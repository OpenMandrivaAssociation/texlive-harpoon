Name:		texlive-harpoon
Version:	1.0
Release:	1
Summary:	Extra harpoons, using the graphics package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/harpoon
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harpoon.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harpoon.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides over- and under-harpoon symbol commands; the harpoons
may point in either direction, with the hook pointing up or
down. The covered object is provided as an argument to the
commands, so that they have the look of accent commands.

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
%{_texmfdistdir}/tex/latex/harpoon/harpoon.sty
%doc %{_texmfdistdir}/doc/latex/harpoon/harpoon.pdf
%doc %{_texmfdistdir}/doc/latex/harpoon/harpoon.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
