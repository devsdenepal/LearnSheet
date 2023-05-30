# APK decompilers

1. **jadx-gui**: 
   - First famous GUI Java decompiler, you could use it to investigate the Java code from the APK once you have obtained it.
   - Built in Java (multi-platform) and at this moment, it's the recommended one.
   - Just download the latest version and execute it from the bin folder:
     ```
     jadx-gui
     ```
   - Using the GUI you can perform text search, go to the functions definitions (CTRL + left click on the function), and cross-refs (right click --> Find Usage).
   - If you only want the Java code but without using a GUI, a very easy way is to use the jadx CLI tool:
     ```
     jadx app.apk
     ```
   - Some interesting options of jadx (GUI and CLI versions) are:
     ```
     -d <path to output dir>
     --no-res #No resources
     --no-src #No source code
     --no-imports #Always write the entire package name (very useful to know where the function that you might want to hook is)
     ```

2. **GDA**: 
   - A powerful and fast reverse analysis platform that supports basic decompiling operations and many excellent functions like Malicious behavior detection, Privacy leaking detection, Vulnerability detection, Path solving, Packer identification, Variable tracking analysis, Deobfuscation, Python & Java scripts, Device memory extraction, Data decryption and encryption, etc.
   - Only available for Windows.

3. **Bytecode-Viewer**: 
   - Another interesting tool for static analysis.
   - It allows you to decompile the APK using several decompilers at the same time. For example, you can see 2 different Java decompilers and one Smali decompiler. It also allows you to modify the code and export it.
   - One limitation of Bytecode-Viewer is that it doesn't have references or cross-references.

4. **Enjarify**: 
   - A tool for translating Dalvik bytecode to equivalent Java bytecode, allowing Java analysis tools to analyze Android applications.

5. **Dex2jar**: 
   - An older tool that translates Dalvik to Java bytecode.
   - It works well most of the time but may fail or produce incorrect results in some cases.
   - Enjarify is designed to handle more cases compared to Dex2jar, including obscure features or edge cases.

6. **CFR**: 
   - A decompiler that can handle modern Java features (e.g., lambda expressions, try-with-resources, and method references).
   - Written entirely in Java 6, so it works anywhere.
   - It can also decompile class files from other JVM languages back into Java.
   - To use CFR, you can use the following JAR file:
     ```
     java -jar ./cfr.jar "$JARFILE" --outputdir "$OUTDIR"
     ```
     For larger JAR files, you may need to increase the memory allocation pool of the JVM.

7. **Fernflower**: 
   - Part of the IntelliJ IDEA project.
   - Fernflower is an analytical decompiler that outputs the generated .java files in a JAR file.
   - To build and use Fernflower, you need to follow specific instructions. Please refer to the project's GitHub page for details.

8. **Krakatau**: 
   - A decompiler written in Python.
   - It requires external class definitions (libraries) and can handle standard library classes up to Java version 8.
   - You can use Krakatau to decompile JAR files by providing the necessary dependencies using the `-path` flag.
   - Please refer to Krakatau's GitHub page for detailed instructions on usage.

9. **Procyon**: 
   - Once installed, you can use Procyon to decompile JAR files straightforwardly.
   - Usage example:
     ```
     procyon -jar "$JARFILE" -o "$OUTDIR"
     ```

References:
- [jadx-gui GitHub](https://github.com/skylot/jadx)
- [GDA GitHub](https://github.com/charles2gan/GDA-android-reversing-Tool)
- [Bytecode-Viewer GitHub](https://github.com/Konloch/bytecode-viewer)
- [Enjarify GitHub](https://github.com/google/enjarify)
- [CFR GitHub](https://github.com/leibnitz27/cfr)
- [Fernflower GitHub](https://github.com/JetBrains/intellij-community/tree/master/plugins/java-decompiler/engine)
- [Krakatau GitHub](https://github.com/Storyyeller/Krakatau)
- [Procyon GitHub](https://bitbucket.org/mstrobel/procyon)
