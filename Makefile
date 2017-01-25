PKG_NAME := jdk-antlr3
URL := http://repo1.maven.org/maven2/org/antlr/antlr-master/3.5.2/antlr-master-3.5.2.pom
ARCHIVES := http://repo1.maven.org/maven2/org/antlr/antlr3-maven-plugin/3.5.2/antlr3-maven-plugin-3.5.2.jar . \
	http://repo1.maven.org/maven2/org/antlr/antlr3-maven-plugin/3.5.2/antlr3-maven-plugin-3.5.2.pom . \
	http://repo1.maven.org/maven2/org/antlr/antlr-runtime/3.5.2/antlr-runtime-3.5.2.jar . \
	http://repo1.maven.org/maven2/org/antlr/antlr-runtime/3.5.2/antlr-runtime-3.5.2.pom . \
	http://repo1.maven.org/maven2/org/antlr/antlr/3.5.2/antlr-3.5.2.jar . \
	http://repo1.maven.org/maven2/org/antlr/antlr/3.5.2/antlr-3.5.2.pom .

include ../common/Makefile.common
