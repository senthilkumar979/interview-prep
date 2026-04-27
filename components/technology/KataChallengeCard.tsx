import { KataItem } from "@/components/technology/moduleData.types";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface KataChallengeCardProps {
  item: KataItem;
}

export const KataChallengeCard = ({ item }: KataChallengeCardProps) => (
  <Card>
    <CardHeader className="space-y-3">
      <CardTitle className="text-lg">{item.title}</CardTitle>
      <div className="flex flex-wrap gap-2">
        <Badge className="px-2 py-1 text-xs font-medium" variant="outline">
          {item.difficulty}
        </Badge>
        <Badge className="px-2 py-1 text-xs font-medium" variant="outline">
          {item.category}
        </Badge>
      </div>
    </CardHeader>
    <CardContent className="space-y-4 text-sm">
      <div className="rounded-md border border-border/70 bg-muted/30 p-3">
        <p className="font-medium">Description</p>
        <p className="mt-1 text-muted-foreground">{item.description}</p>
      </div>
      <div className="rounded-md border border-border/70 bg-muted/30 p-3">
        <p className="font-medium">Requirements</p>
        <ul className="mt-1 list-disc space-y-1 pl-5 text-muted-foreground">
          {item.requirements.map((requirement) => (
            <li key={requirement}>{requirement}</li>
          ))}
        </ul>
      </div>
    </CardContent>
  </Card>
);
