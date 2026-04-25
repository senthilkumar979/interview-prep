"use client";

import Link from "next/link";
import { useState } from "react";
import { MarkdownContent } from "@/components/shared/MarkdownContent";
import { QuestionItem } from "@/components/technology/moduleData.types";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface QuestionCardProps {
  item: QuestionItem;
}

export const QuestionCard = ({ item }: QuestionCardProps) => {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <div className="space-y-3">
      <Card>
        <CardHeader className="space-y-3">
          <div className="flex flex-wrap gap-2">
            <Badge variant="outline">{item.difficulty}</Badge>
            <Badge variant="outline">{item.category}</Badge>
          </div>
          <CardTitle className="text-lg">{item.question}</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4 text-sm">
          <p className="text-muted-foreground">{item.preview}</p>
          <Button onClick={() => setIsExpanded((current) => !current)} type="button" variant="outline">
            {isExpanded ? "Hide Answer" : "Show Answer"}
          </Button>
        </CardContent>
      </Card>

      {isExpanded ? (
        <>
          <Card>
            <CardHeader>
              <CardTitle className="text-base">Deep explanation</CardTitle>
            </CardHeader>
            <CardContent>
              <MarkdownContent content={item.answer} />
            </CardContent>
          </Card>

          {item.examples.map((example, index) => (
            <Card key={example.title}>
              <CardHeader className="space-y-2">
                <CardTitle className="text-base">Code example #{index + 1}</CardTitle>
                <p className="text-xs text-muted-foreground">{example.title}</p>
              </CardHeader>
              <CardContent className="space-y-3">
                <MarkdownContent content={`\`\`\`${example.language}\n${example.code}\n\`\`\``} />
                <div className="rounded-md border border-border/70 bg-muted/30 p-3 text-sm text-muted-foreground">
                  {example.explanation}
                </div>
              </CardContent>
            </Card>
          ))}

          <Card>
            <CardHeader>
              <CardTitle className="text-base">Tip</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="rounded-md border border-border/70 bg-muted/30 p-3 text-sm text-muted-foreground">{item.tip}</p>
            </CardContent>
          </Card>

          {item.links?.length ? (
            <Card>
              <CardHeader>
                <CardTitle className="text-base">Links</CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="list-disc space-y-1 pl-5">
                  {item.links.map((link) => (
                    <li key={link.href}>
                      <Link className="text-primary underline-offset-2 hover:underline" href={link.href}>
                        {link.label}
                      </Link>
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          ) : null}
        </>
      ) : null}
    </div>
  );
};
