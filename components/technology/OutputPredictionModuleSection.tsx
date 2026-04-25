import { OutputPredictionItem } from "@/components/technology/moduleData.types";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface OutputPredictionModuleSectionProps {
  items: OutputPredictionItem[];
}

export const OutputPredictionModuleSection = ({ items }: OutputPredictionModuleSectionProps) => (
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
          <p className="rounded-md border border-border/70 bg-muted/30 p-3 text-muted-foreground">
            Expected output: {item.expectedOutput}
          </p>
          <p className="text-muted-foreground">{item.explanation}</p>
        </CardContent>
      </Card>
    ))}
  </div>
);
