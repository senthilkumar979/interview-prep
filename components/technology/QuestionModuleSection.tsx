import { QuestionItem } from "@/components/technology/moduleData.types";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface QuestionModuleSectionProps {
  items: QuestionItem[];
}

export const QuestionModuleSection = ({ items }: QuestionModuleSectionProps) => (
  <div className="space-y-4">
    {items.map((item) => (
      <Card key={item.id}>
        <CardHeader className="space-y-2">
          <CardTitle className="text-lg">{item.question}</CardTitle>
          <div className="flex flex-wrap gap-2">
            <Badge variant="outline">{item.difficulty}</Badge>
            <Badge variant="outline">{item.category}</Badge>
            {item.tags.map((tag) => (
              <Badge key={tag} variant="secondary">
                {tag}
              </Badge>
            ))}
          </div>
        </CardHeader>
        <CardContent className="space-y-3 text-sm">
          <div>
            <p className="font-medium">Answer</p>
            <p className="text-muted-foreground">{item.answer}</p>
          </div>
          <div>
            <p className="font-medium">Examples</p>
            <ul className="list-disc space-y-1 pl-5 text-muted-foreground">
              {item.examples.map((example) => (
                <li key={example}>{example}</li>
              ))}
            </ul>
          </div>
          <p className="rounded-md border border-border/70 bg-muted/30 p-3 text-muted-foreground">
            Tip: {item.tip}
          </p>
        </CardContent>
      </Card>
    ))}
  </div>
);
