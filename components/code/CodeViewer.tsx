"use client";

import Editor from "@monaco-editor/react";

interface CodeViewerProps {
  code: string;
  language?: string;
}

const codeThemeId = "interviewforge-dark";

export const CodeViewer = ({ code, language = "typescript" }: CodeViewerProps) => (
  <div className="overflow-hidden rounded-lg border border-border">
    <Editor
      beforeMount={(monaco) => {
        monaco.editor.defineTheme(codeThemeId, {
          base: "vs-dark",
          inherit: true,
          rules: [],
          colors: {
            "editor.background": "#0B1020",
            "editor.lineHighlightBackground": "#1A2238",
            "editor.selectionBackground": "#1E3A8A",
            "editorCursor.foreground": "#3B82F6",
          },
        });
      }}
      defaultLanguage={language}
      defaultValue={code}
      height="360px"
      options={{
        fontSize: 13,
        minimap: { enabled: false },
        readOnly: true,
        scrollBeyondLastLine: false,
        wordWrap: "on",
      }}
      theme={codeThemeId}
    />
  </div>
);
