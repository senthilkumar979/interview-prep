"use client";

import { useMemo } from "react";
import { Badge } from "@/components/ui/badge";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { SidebarContent, SidebarGroup, SidebarGroupContent, SidebarGroupLabel, SidebarInput } from "@/components/ui/sidebar";
import { LandingContent } from "@/components/layout/interviewWorkspace.types";

interface SidebarFiltersProps {
  content: LandingContent;
  searchQuery: string;
  onSearchChange: (value: string) => void;
  difficultyFilter: string;
  onDifficultyChange: (value: string) => void;
  categoryFilter: string;
  onCategoryChange: (value: string) => void;
}

export const SidebarFilters = ({
  content,
  searchQuery,
  onSearchChange,
  difficultyFilter,
  onDifficultyChange,
  categoryFilter,
  onCategoryChange,
}: SidebarFiltersProps) => {
  const categories = useMemo(
    () => Array.from(new Set(content.questions.map((question) => question.category))),
    [content.questions],
  );

  return (
    <SidebarContent>
      <SidebarGroup>
        <SidebarGroupLabel>Search</SidebarGroupLabel>
        <SidebarGroupContent>
          <SidebarInput value={searchQuery} onChange={(event) => onSearchChange(event.target.value)} placeholder="Find topics..." />
        </SidebarGroupContent>
      </SidebarGroup>
      <SidebarGroup>
        <SidebarGroupLabel>Difficulty</SidebarGroupLabel>
        <SidebarGroupContent>
          <Select value={difficultyFilter} onValueChange={onDifficultyChange}>
            <SelectTrigger>
              <SelectValue placeholder="Select difficulty" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All</SelectItem>
              <SelectItem value="easy">Easy</SelectItem>
              <SelectItem value="medium">Medium</SelectItem>
              <SelectItem value="hard">Hard</SelectItem>
            </SelectContent>
          </Select>
        </SidebarGroupContent>
      </SidebarGroup>
      <SidebarGroup>
        <SidebarGroupLabel>Category</SidebarGroupLabel>
        <SidebarGroupContent>
          <Select value={categoryFilter} onValueChange={onCategoryChange}>
            <SelectTrigger>
              <SelectValue placeholder="Select category" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All</SelectItem>
              {categories.map((category) => (
                <SelectItem key={category} value={category}>
                  {category}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </SidebarGroupContent>
      </SidebarGroup>
      <SidebarGroup>
        <SidebarGroupLabel>Technologies</SidebarGroupLabel>
        <SidebarGroupContent>
          <div className="flex flex-col gap-2 p-1">
            {content.technologies.map((technology) => (
              <Badge key={technology} className="w-fit" variant="outline">
                {technology}
              </Badge>
            ))}
          </div>
        </SidebarGroupContent>
      </SidebarGroup>
    </SidebarContent>
  );
};
