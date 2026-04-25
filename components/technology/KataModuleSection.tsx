import { KataItem } from "@/components/technology/moduleData.types";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface KataModuleSectionProps {
  items: KataItem[];
}

export const KataModuleSection = ({ items }: KataModuleSectionProps) => (
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
          <p className="text-muted-foreground">{item.description}</p>
          <div className="rounded-md border border-border/70 bg-muted/30 p-3">
            <p className="font-medium">Starter Code</p>
            <p className="text-muted-foreground">{item.starterCode}</p>
          </div>
          <div className="rounded-md border border-border/70 bg-muted/30 p-3">
            <p className="font-medium">Solution</p>
            <p className="text-muted-foreground">{item.solution}</p>
          </div>
        </CardContent>
      </Card>
    ))}
  </div>
);
