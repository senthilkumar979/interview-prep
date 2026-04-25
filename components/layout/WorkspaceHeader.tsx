"use client";

import { Search } from "lucide-react";
import { ThemeToggle } from "@/components/layout/ThemeToggle";
import { Breadcrumb, BreadcrumbItem, BreadcrumbList, BreadcrumbPage, BreadcrumbSeparator } from "@/components/ui/breadcrumb";
import { Input } from "@/components/ui/input";
import { SidebarTrigger } from "@/components/ui/sidebar";

interface WorkspaceHeaderProps {
  searchQuery: string;
  onSearchChange: (value: string) => void;
}

export const WorkspaceHeader = ({ searchQuery, onSearchChange }: WorkspaceHeaderProps) => (
  <header className="sticky top-0 z-20 flex h-16 items-center justify-between border-b bg-background/95 px-4 backdrop-blur md:px-6">
    <div className="flex items-center gap-3">
      <SidebarTrigger />
      <Breadcrumb>
        <BreadcrumbList>
          <BreadcrumbItem>Dashboard</BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbPage>Question Bank</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>
    </div>
    <div className="flex items-center gap-2">
      <div className="relative hidden w-64 md:block">
        <Search className="pointer-events-none absolute top-2.5 left-2 h-4 w-4 text-muted-foreground" />
        <Input className="pl-8" value={searchQuery} onChange={(event) => onSearchChange(event.target.value)} placeholder="Search questions..." />
      </div>
      <ThemeToggle />
    </div>
  </header>
);
