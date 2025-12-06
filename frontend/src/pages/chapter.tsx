import React, { useState, useEffect } from 'react';
import Layout from '@theme/Layout';
import { useLocation } from '@docusaurus/router';

interface Chapter {
  id: string;
  title: string;
  content: string;
  module_id: string;
  week_number: number;
  learning_objectives: string[];
  prerequisites: string[];
  estimated_duration: number;
  difficulty: string;
  created_at: string;
  updated_at: string;
}

const ChapterPage: React.FC = () => {
  const [chapter, setChapter] = useState<Chapter | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const location = useLocation();

  // Extract chapter ID from URL query parameter
  const searchParams = new URLSearchParams(location.search);
  const chapterId = searchParams.get('id');

  useEffect(() => {
    const fetchChapter = async () => {
      if (!chapterId) {
        setError('No chapter ID provided');
        setLoading(false);
        return;
      }

      try {
        const response = await fetch(`/api/chapters/${chapterId}`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setChapter(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'An error occurred');
      } finally {
        setLoading(false);
      }
    };

    fetchChapter();
  }, [chapterId]);

  if (loading) {
    return (
      <Layout title="Loading Chapter...">
        <div className="container margin-vert--xl">
          <div className="row">
            <div className="col col--6 col--offset-3">
              <h1>Loading Chapter...</h1>
              <p>Please wait while we load the chapter content.</p>
            </div>
          </div>
        </div>
      </Layout>
    );
  }

  if (error) {
    return (
      <Layout title="Error Loading Chapter">
        <div className="container margin-vert--xl">
          <div className="row">
            <div className="col col--6 col--offset-3">
              <h1>Error Loading Chapter</h1>
              <p>Error: {error}</p>
            </div>
          </div>
        </div>
      </Layout>
    );
  }

  return (
    <Layout title={chapter?.title || "Chapter"}>
      <div className="container margin-vert--lg">
        <div className="row">
          <div className="col col--8 col--offset-2">
            {chapter ? (
              <article className="margin-vert--lg">
                <header>
                  <h1>{chapter.title}</h1>
                  <div className="margin-vert--md">
                    <span className="badge badge--secondary">Week {chapter.week_number}</span>
                    <span className="badge badge--info margin-left--sm">{chapter.difficulty}</span>
                  </div>
                </header>

                <section className="margin-vert--lg">
                  <h2>Learning Objectives</h2>
                  <ul>
                    {chapter.learning_objectives.map((objective, index) => (
                      <li key={index}>{objective}</li>
                    ))}
                  </ul>
                </section>

                <section className="margin-vert--lg">
                  <h2>Content</h2>
                  <div dangerouslySetInnerHTML={{ __html: chapter.content }} />
                </section>

                {chapter.prerequisites.length > 0 && (
                  <section className="margin-vert--lg">
                    <h2>Prerequisites</h2>
                    <ul>
                      {chapter.prerequisites.map((prereq, index) => (
                        <li key={index}>{prereq}</li>
                      ))}
                    </ul>
                  </section>
                )}

                <footer className="margin-vert--lg">
                  <div className="text--right">
                    <small>
                      Estimated duration: {chapter.estimated_duration} hours •
                      Last updated: {new Date(chapter.updated_at).toLocaleDateString()}
                    </small>
                  </div>
                </footer>
              </article>
            ) : (
              <div>
                <h1>Chapter Not Found</h1>
                <p>The requested chapter could not be found.</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default ChapterPage;