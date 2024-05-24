# Koushik Krishnan's Resume

from resume_builder import Resume, Section, SectionEntry, ContactInfo, ConcatText, ItalicsText, UnderlinedText, LinkText, BulletedList

resume = Resume(
    contact_info=ContactInfo(
        name="Koushik Krishnan",
        details=[
            "(111) 111-1111",
            "my@email.com",
            LinkText("koushik.bearblog.dev", "https://koushik.bearblog.dev"),
            LinkText(
                "linkedin.com/in/koushikkrishnan",
                "https://www.linkedin.com/in/koushikkrishnan/",
            ),
            LinkText("github.com/koek67", "https://www.github.com/koek67"),
        ],
        tag_line="Making software as reliable as the sunrise.",
    ),
    sections = [
        Section(
            title="Experience",
            entries=[
                SectionEntry(
                    title=LinkText("Microsoft", "https://www.microsoft.com"),
                    caption="Senior Software Engineer",
                    location="Remote",
                    dates="February 2023 - present",
                    description=BulletedList(
                        [
                            "Building reliability improvements into the storage and replication layers of Cosmos DB.",
                            "Technical lead for a team of engineers, ramping them up on distributed systems and database concepts as well as preparing them for incident response.",
                        ]
                    ),
                ),
                SectionEntry(
                    title=LinkText("Yugabyte", "https://www.yugabyte.com"),
                    caption="Senior Site Reliability Engineer",
                    location="Seattle, Washington",
                    dates="May 2022 - February 2023",
                    description=BulletedList(
                        [
                            "Managed reliable operation of Kubernetes and Yugabyte database clusters across AWS and GCP for the Yugabyte Managed product."
                        ]
                    ),
                ),
                SectionEntry(
                    title=LinkText("Microsoft", "https://www.microsoft.com"),
                    caption="Software Engineer 2, Azure Cosmos DB",
                    location="Redmond, Washington",
                    dates="August 2018 - April 2022",
                    description=BulletedList(
                        [
                            "Worked as a technical lead for a petabyte-scale, globally distributed database. Reduced number of production incidents by 80%.",
                            'Founded a team that built a Python microservice that would perform real-time root cause analysis/mitigation of incidents and eliminate the need for an on-call engineer. Open sourced this work on Github as <a class="open-link" target="_blank" href="http://github.com/microsoft/jupyrest">Jupyrest</a>',
                        ]
                    ),
                ),
                SectionEntry(
                    title=LinkText("Microsoft", "https://www.microsoft.com"),
                    caption="Software Engineering Intern, Azure Cosmos DB",
                    location="Seattle, Washington",
                    dates="May 2017 - August 2017",
                ),
                SectionEntry(
                    title=LinkText("Fitbit", "https://fitbit.com"),
                    caption="Software Engineering Intern",
                    location="Boston, Massachusetts",
                    dates="May 2016 - August 2016",
                ),
                SectionEntry(
                    title=LinkText("Kayak.com", "https://www.kayak.com"),
                    caption="Software Engineering Intern",
                    location="Concord, Massachusetts",
                    dates="May 2015 - August 2015",
                )
            ],
        ),
        Section(
            title="Presentations",
            entries=[
                SectionEntry(
                    title=LinkText(
                        text="PyCon 2024",
                        url="https://us.pycon.org/2024/schedule/presentation/95/",
                        show_icon=True,
                    ),
                    caption="Rest East with Jupyrest: Deploy notebooks as web services",
                    location="Pittsburgh, PA",
                    dates="May 2024",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyTexas",
                        url="https://www.pytexas.org/2024/schedule/talks/#rest-easy-with-jupyrest-deploy-notebooks-as-web-services",
                        show_icon=True,
                    ),
                    caption="Rest East with Jupyrest",
                    location="Austin, TX",
                    dates="April 2024",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyCascades",
                        url="https://2024.pycascades.com/program/talks/jupyrest/",
                        show_icon=True,
                    ),
                    caption="Rest East with Jupyrest: Deploy notebooks as web services",
                    location="Seattle, WA",
                    dates="April 2024",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyOhio 2023",
                        url="https://www.pyohio.org/2023/speakers/koushik-krishnan/",
                        show_icon=True,
                    ),
                    caption=LinkText('Serverless Jupyter Notebook Functions (YouTube)', url="https://youtu.be/hoGJ0c3jIeo?si=srbRtjSxOxETFWN5", show_icon=True),
                    location="Virtual",
                    dates="December 2023",
                ),
                SectionEntry(
                    title=LinkText(
                        text="PyData Seattle 2023",
                        url="https://seattle2023.pydata.org/cfp/talk/K8KV8M/",
                        show_icon=True,
                    ),
                    caption=LinkText('Notebooks as Serverless Functions (YouTube)', url="https://youtu.be/hoGJ0c3jIeo?si=srbRtjSxOxETFWN5", show_icon=True),
                    location="Seattle, WA",
                    dates="April 2023",
                ),
            ],
        ),
        Section(
            title="Volunteering",
            entries=[
                SectionEntry(
                    title=LinkText(
                        "ASHA Chennai", url="https://chennai.ashanet.org/", show_icon=True
                    ),
                    caption="Spoken English Teacher",
                    location="Remote",
                    dates="December 2020 - March 2022",
                    description=BulletedList(
                        [
                            "Created a curriculum with story-telling, skits, and friendly debates to provide disadvantaged children isolated in quarantine a fun way to learn spoken English.",
                        ]
                    ),
                )
            ],
        ),
        Section(
            title="Education",
            entries=[
                SectionEntry(
                    title="Georgia Institute of Technology",
                    location="Atlanta, Georgia",
                    dates="August 2014 - May 2018",
                    description=ItalicsText(
                        "Bachelors of Science in Computer Science and Mathematics"
                    ),
                )
            ],
        ),
        Section(
            title="Skills",
            entries=[
                SectionEntry(
                    description=BulletedList(
                        [
                            ConcatText(
                                UnderlinedText("Languages:"),
                                " Python, Golang, C/C++, JavaScript, C#, Powershell, Zig",
                            ),
                            ConcatText(
                                UnderlinedText("Tools:"),
                                " Kubernetes, PostgreSQL, Linux, Windows, Azure Service Fabric, Distributed Databases, Storage Engines, Docker",
                            ),
                        ]
                    )
                ),
            ],
        ),
    ]
)

if __name__ == "__main__":
    resume.cli_main()