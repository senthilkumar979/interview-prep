"use client";

import { useMemo, useState } from "react";
import { QuestionGrid } from "@/components/layout/QuestionGrid";
import { SidebarFilters } from "@/components/layout/SidebarFilters";
import { LandingContent } from "@/components/layout/interviewWorkspace.types";
import { WorkspaceHeader } from "@/components/layout/WorkspaceHeader";
import { Sidebar, SidebarHeader, SidebarInset, SidebarProvider } from "@/components/ui/sidebar";

interface InterviewWorkspaceProps {
  content: LandingContent;
}

export const InterviewWorkspace = ({ content }: InterviewWorkspaceProps) => {
  const [searchQuery, setSearchQuery] = useState("");
  const [difficultyFilter, setDifficultyFilter] = useState("all");
  const [categoryFilter, setCategoryFilter] = useState("all");

  const filteredQuestions = useMemo(
    () =>
      content.questions.filter((question) => {
        const matchesSearch =
          question.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
          question.description.toLowerCase().includes(searchQuery.toLowerCase()) ||
          question.technology.toLowerCase().includes(searchQuery.toLowerCase());
        const matchesDifficulty = difficultyFilter === "all" || question.difficulty === difficultyFilter;
        const matchesCategory = categoryFilter === "all" || question.category === categoryFilter;
        return matchesSearch && matchesDifficulty && matchesCategory;
      }),
    [categoryFilter, content.questions, difficultyFilter, searchQuery],
  );

  return (
    <SidebarProvider defaultOpen>
      <Sidebar collapsible="offcanvas">
        <SidebarHeader>
          <div className="rounded-md border border-sidebar-border bg-sidebar-accent p-3">
            <p className="font-semibold text-sidebar-accent-foreground">{content.brand.name}</p>
            <p className="text-xs text-sidebar-foreground/70">{content.brand.tagline}</p>
          </div>
        </SidebarHeader>
        <SidebarFilters
          categoryFilter={categoryFilter}
          content={content}
          difficultyFilter={difficultyFilter}
          onCategoryChange={setCategoryFilter}
          onDifficultyChange={setDifficultyFilter}
          onSearchChange={setSearchQuery}
          searchQuery={searchQuery}
        />
      </Sidebar>

      <SidebarInset className="min-h-svh">
        <WorkspaceHeader onSearchChange={setSearchQuery} searchQuery={searchQuery} />
        <QuestionGrid questions={filteredQuestions} />
      </SidebarInset>
    </SidebarProvider>
  );
};
