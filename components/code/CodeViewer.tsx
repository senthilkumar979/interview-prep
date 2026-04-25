"use client";

import Editor from "@monaco-editor/react";

interface CodeViewerProps {
  code: string;
  language?: string;
}

export const CodeViewer = ({ code, language = "typescript" }: CodeViewerProps) => (
  <div className="overflow-hidden rounded-lg border border-border">
    <Editor
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
      theme="vs-dark"
    />
  </div>
);
