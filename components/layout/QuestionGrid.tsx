"use client";

import { CodeViewer } from "@/components/code/CodeViewer";
import { InterviewQuestion } from "@/components/layout/interviewWorkspace.types";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface QuestionGridProps {
  questions: InterviewQuestion[];
}

export const QuestionGrid = ({ questions }: QuestionGridProps) => (
  <main className="grid gap-4 p-4 md:grid-cols-2 md:p-6">
    {questions.map((question) => (
      <Card key={question.id}>
        <CardHeader className="space-y-2">
          <div className="flex flex-wrap items-center gap-2">
            <Badge variant="secondary">{question.difficulty}</Badge>
            <Badge variant="outline">{question.category}</Badge>
            <Badge variant="outline">{question.technology}</Badge>
          </div>
          <CardTitle className="text-lg">{question.title}</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <p className="text-sm text-muted-foreground">{question.description}</p>
          <CodeViewer code={question.snippet} />
        </CardContent>
      </Card>
    ))}
    {questions.length === 0 ? (
      <Card className="md:col-span-2">
        <CardContent className="pt-6 text-sm text-muted-foreground">
          No questions found. Try changing search, difficulty, or category filters.
        </CardContent>
      </Card>
    ) : null}
  </main>
);
