import { RapidFireItem } from "@/components/technology/moduleData.types";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface RapidFireModuleSectionProps {
  items: RapidFireItem[];
}

export const RapidFireModuleSection = ({ items }: RapidFireModuleSectionProps) => (
  <div className="space-y-4">
    {items.map((item) => (
      <Card key={item.id}>
        <CardHeader className="space-y-2">
          <CardTitle className="text-lg">{item.prompt}</CardTitle>
          <div className="flex flex-wrap gap-2">
            <Badge variant="outline">{item.difficulty}</Badge>
            <Badge variant="outline">{item.category}</Badge>
          </div>
        </CardHeader>
        <CardContent className="space-y-2 text-sm">
          <p className="text-muted-foreground">Expected answer:</p>
          <p className="rounded-md border border-border/70 bg-muted/30 p-3 text-muted-foreground">{item.expectedAnswer}</p>
        </CardContent>
      </Card>
    ))}
  </div>
);
