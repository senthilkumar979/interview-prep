import ReactMarkdown from 'react-markdown'
import rehypeHighlight from 'rehype-highlight'

interface MarkdownContentProps {
  content: string
  className?: string
}

export const MarkdownContent = ({ content, className = '' }: MarkdownContentProps) => (
  <div
    className={`prose prose-sm max-w-none rounded-xl prose-p:text-muted-foreground prose-strong:text-foreground prose-pre:max-w-full prose-pre:overflow-x-auto prose-code:whitespace-pre dark:prose-invert ${className}`}
  >
    <ReactMarkdown rehypePlugins={[rehypeHighlight]}>{content}</ReactMarkdown>
  </div>
)
