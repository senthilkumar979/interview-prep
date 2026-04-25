import { DebugItem } from "@/components/technology/moduleData.types";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface DebugModuleSectionProps {
  items: DebugItem[];
}

export const DebugModuleSection = ({ items }: DebugModuleSectionProps) => (
  <div className="space-y-4">
    {items.map((item) => (
      <Card key={item.id}>
        <CardHeader className="space-y-2">
          <CardTitle className="text-lg">{item.title}</CardTitle>
          <div className="flex flex-wrap gap-2">
            <Badge variant="outline">{item.difficulty}</Badge>
            <Badge variant="outline">{item.category}</Badge>
            <Badge variant="secondary">File: {item.file}</Badge>
          </div>
        </CardHeader>
        <CardContent className="space-y-3 text-sm">
          {item.answers.map((answer) => (
            <div key={`${item.id}-${answer.line}`} className="rounded-md border border-border/70 bg-muted/30 p-3">
              <p className="font-medium">
                Line {answer.line}: {answer.title}
              </p>
              <p className="mt-1 text-muted-foreground">{answer.explanation}</p>
              <p className="mt-2 text-muted-foreground">Fix: {answer.fix}</p>
            </div>
          ))}
        </CardContent>
      </Card>
    ))}
  </div>
);
