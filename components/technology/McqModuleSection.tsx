import { McqItem } from "@/components/technology/moduleData.types";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface McqModuleSectionProps {
  items: McqItem[];
}

export const McqModuleSection = ({ items }: McqModuleSectionProps) => (
  <div className="space-y-4">
    {items.map((item) => (
      <Card key={item.id}>
        <CardHeader className="space-y-2">
          <CardTitle className="text-lg">{item.question}</CardTitle>
          <div className="flex flex-wrap gap-2">
            <Badge variant="outline">{item.difficulty}</Badge>
            <Badge variant="outline">{item.category}</Badge>
          </div>
        </CardHeader>
        <CardContent className="space-y-3 text-sm">
          <ul className="space-y-2">
            {item.options.map((option) => (
              <li key={option.id} className="rounded-md border border-border/70 p-2 text-muted-foreground">
                {option.id}. {option.text}
              </li>
            ))}
          </ul>
          <p className="text-muted-foreground">Correct: {item.correctOptionId}</p>
          <p className="rounded-md border border-border/70 bg-muted/30 p-3 text-muted-foreground">{item.explanation}</p>
        </CardContent>
      </Card>
    ))}
  </div>
);
