import Link from "next/link";
import { Atom, Braces, Coffee, LucideIcon } from "lucide-react";
import { TechnologyCategory } from "@/components/home/technology.types";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const iconMap: Record<TechnologyCategory["icon"], LucideIcon> = {
  react: Atom,
  javascript: Braces,
  java: Coffee,
};

interface TechnologyCardProps {
  technology: TechnologyCategory;
}

export const TechnologyCard = ({ technology }: TechnologyCardProps) => {
  const Icon = iconMap[technology.icon] ?? Braces;

  return (
    <Link href={`/${technology.slug}`}>
      <Card className="h-full border-border/70 bg-card hover:border-primary/60">
        <CardHeader className="space-y-3">
          <div className="flex items-center gap-2 text-sm text-muted-foreground">
            <Icon className="h-4 w-4" />
            <span>{technology.title}</span>
          </div>
          <CardTitle className="text-lg">{technology.title}</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <p className="text-sm text-muted-foreground">{technology.description}</p>
          <div className="grid grid-cols-2 gap-2 text-xs">
            <div className="rounded-md border border-border/60 p-2">
              <p className="text-muted-foreground">Questions</p>
              <p className="font-semibold">{technology.questionCount}</p>
            </div>
            <div className="rounded-md border border-border/60 p-2">
              <p className="text-muted-foreground">Exercises</p>
              <p className="font-semibold">{technology.exerciseCount}</p>
            </div>
          </div>
          <div className="flex flex-wrap gap-2">
            <Badge variant="outline">Easy: {technology.difficultyBreakdown.easy}</Badge>
            <Badge variant="outline">Medium: {technology.difficultyBreakdown.medium}</Badge>
            <Badge variant="outline">Hard: {technology.difficultyBreakdown.hard}</Badge>
          </div>
        </CardContent>
      </Card>
    </Link>
  );
};
