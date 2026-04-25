import { SystemDesignItem } from "@/components/technology/moduleData.types";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface SystemDesignModuleSectionProps {
  items: SystemDesignItem[];
}

export const SystemDesignModuleSection = ({ items }: SystemDesignModuleSectionProps) => (
  <div className="space-y-4">
    {items.map((item) => (
      <Card key={item.id}>
        <CardHeader className="space-y-2">
          <CardTitle className="text-lg">{item.title}</CardTitle>
          <div className="flex flex-wrap gap-2">
            <Badge variant="outline">{item.difficulty}</Badge>
            <Badge variant="outline">{item.category}</Badge>
          </div>
        </CardHeader>
        <CardContent className="space-y-3 text-sm">
          <p className="text-muted-foreground">{item.problem}</p>
          <div>
            <p className="font-medium">Requirements</p>
            <ul className="list-disc space-y-1 pl-5 text-muted-foreground">
              {item.requirements.map((requirement) => (
                <li key={requirement}>{requirement}</li>
              ))}
            </ul>
          </div>
          <p className="rounded-md border border-border/70 bg-muted/30 p-3 text-muted-foreground">{item.approach}</p>
        </CardContent>
      </Card>
    ))}
  </div>
);
