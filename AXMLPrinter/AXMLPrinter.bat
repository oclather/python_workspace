:AXMLprinter
@set /p filepath=请拖入要解密的XML文件:

@echo off

set new_xml=%filepath:AndroidManifest.xml=Manifest.txt%  

java -jar AXMLPrinter2.jar  %filepath% > %new_xml%

%new_xml%
@echo XML文件解密成功！
@goto :AXMLprinter

