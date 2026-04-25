import { FillItem } from "@/components/technology/moduleData.types";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface FillModuleSectionProps {
  items: FillItem[];
}

export const FillModuleSection = ({ items }: FillModuleSectionProps) => (
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
                Line {answer.line}: {answer.placeholder}
              </p>
              <p className="mt-1 text-muted-foreground">Answer: {answer.value}</p>
              <p className="mt-1 text-muted-foreground">{answer.explanation}</p>
            </div>
          ))}
        </CardContent>
      </Card>
    ))}
  </div>
);
