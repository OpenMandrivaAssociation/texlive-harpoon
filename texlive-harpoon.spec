# revision 21327
# category Package
# catalog-ctan /macros/latex/contrib/harpoon
# catalog-date 2008-09-24 00:41:06 +0200
# catalog-license pd
# catalog-version 1.0
Name:		texlive-harpoon
Version:	1.0
Release:	2
Summary:	Extra harpoons, using the graphics package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/harpoon
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harpoon.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harpoon.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides over- and under-harpoon symbol commands; the harpoons
may point in either direction, with the hook pointing up or
down. The covered object is provided as an argument to the
commands, so that they have the look of accent commands.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752476
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718602
- texlive-harpoon
- texlive-harpoon
- texlive-harpoon
- texlive-harpoon

