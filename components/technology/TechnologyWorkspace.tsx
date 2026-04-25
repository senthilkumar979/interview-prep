"use client";

import { ChevronLeft, ChevronRight, FolderTree } from "lucide-react";
import { useMemo, useState } from "react";
import { TechnologyCategory } from "@/components/home/technology.types";
import { AppBreadcrumbs } from "@/components/shared/AppBreadcrumbs";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { TechnologyModuleRenderer } from "@/components/technology/TechnologyModuleRenderer";
import { TechnologyModule, technologyModules } from "@/components/technology/technologyModules";
import { cn } from "@/lib/utils";

interface TechnologyWorkspaceProps {
  technology: TechnologyCategory;
}

export const TechnologyWorkspace = ({ technology }: TechnologyWorkspaceProps) => {
  const [isMenuCollapsed, setIsMenuCollapsed] = useState(false);
  const [selectedModule, setSelectedModule] = useState<TechnologyModule>("Interview Questions");

  const moduleSummary = useMemo(
    () =>
      `${technology.title} · ${selectedModule} · ${technology.questionCount} questions · ${technology.exerciseCount} exercises`,
    [selectedModule, technology.exerciseCount, technology.questionCount, technology.title],
  );

  return (
    <main className="min-h-svh bg-background">
      <div className="flex">
        <aside
          className={cn(
            "sticky top-0 h-svh border-r border-border/70 bg-card",
            isMenuCollapsed ? "w-16" : "w-72",
          )}
        >
          <div className="flex items-center justify-between border-b border-border/70 p-3">
            {!isMenuCollapsed ? <p className="text-sm font-semibold">{technology.title}</p> : null}
            <Button
              aria-label="Toggle module menu"
              onClick={() => setIsMenuCollapsed((previous) => !previous)}
              size="icon-sm"
              type="button"
              variant="ghost"
            >
              {isMenuCollapsed ? <ChevronRight className="h-4 w-4" /> : <ChevronLeft className="h-4 w-4" />}
            </Button>
          </div>

          <nav className="p-2">
            {technologyModules.map((module) => {
              const isActive = selectedModule === module;
              return (
                <button
                  key={module}
                  className={cn(
                    "mb-1 flex w-full items-center gap-2 rounded-md px-2 py-2 text-left text-sm",
                    "hover:bg-accent hover:text-accent-foreground",
                    isActive ? "bg-accent text-accent-foreground" : "text-muted-foreground",
                  )}
                  onClick={() => setSelectedModule(module)}
                  type="button"
                >
                  <FolderTree className="h-4 w-4 shrink-0" />
                  {!isMenuCollapsed ? <span>{module}</span> : null}
                </button>
              );
            })}
          </nav>
        </aside>

        <section className="w-full p-4 md:p-6">
          <div className="mb-4 rounded-lg border border-border/70 bg-card p-4">
            <AppBreadcrumbs
              items={[
                { label: "Technologies", href: "/" },
                { label: technology.title, href: `/${technology.slug}` },
                { label: selectedModule },
              ]}
            />
          </div>

          <Card>
            <CardHeader className="space-y-3">
              <CardTitle className="text-2xl">{selectedModule}</CardTitle>
              <div className="flex flex-wrap gap-2">
                <Badge variant="outline">Technology: {technology.title}</Badge>
                <Badge variant="outline">Questions: {technology.questionCount}</Badge>
                <Badge variant="outline">Exercises: {technology.exerciseCount}</Badge>
              </div>
            </CardHeader>
            <CardContent className="space-y-4">
              <p className="text-sm text-muted-foreground">{moduleSummary}</p>
              <TechnologyModuleRenderer module={selectedModule} />
            </CardContent>
          </Card>
        </section>
      </div>
    </main>
  );
};
