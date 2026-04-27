import { DebugModuleSection } from "@/components/technology/DebugModuleSection";
import { FillModuleSection } from "@/components/technology/FillModuleSection";
import { KataModuleSection } from "@/components/technology/KataModuleSection";
import { McqModuleSection } from "@/components/technology/McqModuleSection";
import { OutputPredictionModuleSection } from "@/components/technology/OutputPredictionModuleSection";
import { QuestionModuleSection } from "@/components/technology/QuestionModuleSection";
import { RapidFireModuleSection } from "@/components/technology/RapidFireModuleSection";
import { SystemDesignModuleSection } from "@/components/technology/SystemDesignModuleSection";
import {
  DebugItem,
  FillItem,
  KataItem,
  McqItem,
  OutputPredictionItem,
  QuestionItem,
  RapidFireItem,
  SystemDesignItem,
} from "@/components/technology/moduleData.types";
import { TechnologyModule } from "@/components/technology/technologyModules";
import debugItems from "@/content/modules/debug.json";
import fillItems from "@/content/modules/fill.json";
import javascriptQuestionItems from "@/content/modules/javascript/questions.json";
import kataItems from "@/content/modules/kata.json";
import mcqItems from "@/content/modules/mcq.json";
import outputPredictionItems from "@/content/modules/output-prediction.json";
import questionItems from "@/content/modules/question.json";
import rapidFireItems from "@/content/modules/rapid-fire.json";
import systemDesignItems from "@/content/modules/system-design.json";

interface TechnologyModuleRendererProps {
  module: TechnologyModule;
  technologySlug: "react" | "javascript" | "java";
}

export const TechnologyModuleRenderer = ({ module, technologySlug }: TechnologyModuleRendererProps) => {
  if (module === "Interview Questions") {
    const interviewQuestions =
      technologySlug === "javascript" ? (javascriptQuestionItems as QuestionItem[]) : (questionItems as QuestionItem[]);
    return <QuestionModuleSection items={interviewQuestions} />;
  }
  if (module === "Coding Exercises") return <KataModuleSection items={kataItems as KataItem[]} />;
  if (module === "Debugging") return <DebugModuleSection items={debugItems as DebugItem[]} />;
  if (module === "Fill in blanks") return <FillModuleSection items={fillItems as FillItem[]} />;
  if (module === "MCQ") return <McqModuleSection items={mcqItems as McqItem[]} />;
  if (module === "Rapid Fire") return <RapidFireModuleSection items={rapidFireItems as RapidFireItem[]} />;
  if (module === "Output prediction")
    return <OutputPredictionModuleSection items={outputPredictionItems as OutputPredictionItem[]} />;
  return <SystemDesignModuleSection items={systemDesignItems as SystemDesignItem[]} />;
};
