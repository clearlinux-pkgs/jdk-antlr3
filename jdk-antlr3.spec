Name     : jdk-antlr3
Version  : 3.5.2
Release  : 1
URL      : http://repo1.maven.org/maven2/org/antlr/antlr-master/3.5.2/antlr-master-3.5.2.pom
Source0  : http://repo1.maven.org/maven2/org/antlr/antlr-master/3.5.2/antlr-master-3.5.2.pom
Source1  : http://repo1.maven.org/maven2/org/antlr/antlr-runtime/3.5.2/antlr-runtime-3.5.2.jar
Source2  : http://repo1.maven.org/maven2/org/antlr/antlr-runtime/3.5.2/antlr-runtime-3.5.2.pom
Source3  : http://repo1.maven.org/maven2/org/antlr/antlr/3.5.2/antlr-3.5.2.jar
Source4  : http://repo1.maven.org/maven2/org/antlr/antlr/3.5.2/antlr-3.5.2.pom
Source5  : http://repo1.maven.org/maven2/org/antlr/antlr3-maven-plugin/3.5.2/antlr3-maven-plugin-3.5.2.jar
Source6  : http://repo1.maven.org/maven2/org/antlr/antlr3-maven-plugin/3.5.2/antlr3-maven-plugin-3.5.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause-Clear
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/maven-poms/antlr3-master.pom

mv %{SOURCE1} %{buildroot}/usr/share/java/antlr3-runtime.jar
mv %{SOURCE2} %{buildroot}/usr/share/maven-poms/antlr3-runtime.pom

mv %{SOURCE3} %{buildroot}/usr/share/java/antlr3.jar
mv %{SOURCE4} %{buildroot}/usr/share/maven-poms/antlr3.pom

mv %{SOURCE5} %{buildroot}/usr/share/java/antlr3-maven-plugin.jar
mv %{SOURCE6} %{buildroot}/usr/share/maven-poms/antlr3-maven-plugin.pom


# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/antlr3.xml \
%{buildroot}/usr/share/maven-poms/antlr3.pom \
%{buildroot}/usr/share/java/antlr3.jar

for a in master runtime maven-plugin
do
	python3 /usr/share/java-utils/maven_depmap.py \
	-n "" \
	--pom-base %{buildroot}/usr/share/maven-poms \
	--jar-base %{buildroot}/usr/share/java \
	%{buildroot}/usr/share/maven-metadata/antlr3-$a.xml \
	%{buildroot}/usr/share/maven-poms/antlr3-$a.pom \
	%{buildroot}/usr/share/java/antlr3-$a.jar
done

%files
%defattr(-,root,root,-)
/usr/share/java/antlr3-maven-plugin.jar
/usr/share/java/antlr3-runtime.jar
/usr/share/java/antlr3.jar
/usr/share/maven-metadata/antlr3-master.xml
/usr/share/maven-metadata/antlr3-maven-plugin.xml
/usr/share/maven-metadata/antlr3-runtime.xml
/usr/share/maven-metadata/antlr3.xml
/usr/share/maven-poms/antlr3-master.pom
/usr/share/maven-poms/antlr3-maven-plugin.pom
/usr/share/maven-poms/antlr3-runtime.pom
/usr/share/maven-poms/antlr3.pom
