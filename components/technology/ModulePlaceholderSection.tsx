interface ModulePlaceholderSectionProps {
  moduleName: string;
}

export const ModulePlaceholderSection = ({ moduleName }: ModulePlaceholderSectionProps) => (
  <div className="rounded-md border border-border/70 bg-muted/30 p-4 text-sm text-muted-foreground">
    {moduleName} component scaffold is ready. Add JSON schema and renderer similar to Question, Kata, Debug, and Fill modules.
  </div>
);
